# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy
import io
import json
import os
import tarfile
import time
import yaml

import docker
import pytest
import requests

from kubernetes import config
from openshift.helper import KubernetesObjectHelper
from openshift.client import models
from openshift.helper.ansible import AnsibleModuleHelper


@pytest.fixture(scope='session')
def openshift_container(request):
    client = docker.from_env()
    # TODO: bind to a random host port
    image_name = 'openshift/origin:{}'.format(request.config.getoption('--openshift-version'))
    container = client.containers.run(image_name, 'start master', detach=True,
                                      ports={'8443/tcp': 8443})

    try:
        # Wait for the container to no longer be in the created state before
        # continuing
        while container.status == u'created':
            time.sleep(0.2)
            container = client.containers.get(container.id)

        # Wait for the api server to be ready before continuing
        for _ in range(10):
            try:
                resp = requests.head("https://127.0.0.1:8443/healthz/ready", verify=False)
            except requests.RequestException:
                pass
            time.sleep(1)

        time.sleep(1)

        yield container
    finally:
        # Always remove the container
        container.remove(force=True)


@pytest.fixture(scope='session')
def kubeconfig(openshift_container, tmpdir_factory):
    # get_archive returns a stream of the tar archive containing the requested
    # files/directories, so we need use BytesIO as an intermediate step.
    tar_stream, _ = openshift_container.get_archive('/var/lib/origin/openshift.local.config/master/admin.kubeconfig')
    tar_obj = tarfile.open(fileobj=io.BytesIO(tar_stream.read()))
    kubeconfig_contents = tar_obj.extractfile('admin.kubeconfig').read()

    kubeconfig_file = tmpdir_factory.mktemp('kubeconfig').join('admin.kubeconfig')
    kubeconfig_file.write(kubeconfig_contents)
    yield kubeconfig_file


@pytest.fixture()
def k8s_helper(request, kubeconfig):
    _, api_version, resource = request.module.__name__.split('_', 2)
    helper = KubernetesObjectHelper(api_version, resource)
    auth = {
        'kubeconfig': str(kubeconfig),
        'host': 'https://localhost:8443',
        'verify_ssl': False
    }
    helper.set_client_config(**auth)
    #config.kube_config.configuration.host = 'https://localhost:8443'
    #config.kube_config.configuration.verify_ssl = False
    yield helper


@pytest.fixture()
def ansible_helper(request, kubeconfig):
    _, api_version, resource = request.module.__name__.split('_', 2)
    helper = AnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False)
    auth = {
        'kubeconfig': str(kubeconfig),
        'host': 'https://localhost:8443',
        'verify_ssl': False
    }
    helper.set_client_config(**auth)
    #config.kube_config.configuration.host = 'https://localhost:8443'
    #config.kube_config.configuration.verify_ssl = False
    yield helper


@pytest.fixture(scope='session')
def obj_compare():
    def compare_func(ansible_helper, k8s_obj, parameters):
        """ Assert that an object matches an expected object """
        requested = copy.deepcopy(k8s_obj)
        ansible_helper.object_from_params(parameters, obj=requested)
        assert ansible_helper.objects_match(k8s_obj, requested)
    return compare_func


@pytest.fixture(scope='session')
def create_namespace():
    def create_func(namespace):
        """ Create a namespace """
        helper = KubernetesObjectHelper('v1', 'namespace')
        k8s_obj = helper.get_object(namespace)
        if not k8s_obj:
            k8s_obj = helper.model()
            k8s_obj.metadata =  models.V1ObjectMeta()
            k8s_obj.metadata.name = namespace
            k8s_obj = helper.create_object(None, k8s_obj)
        assert k8s_obj is not None
    return create_func


@pytest.fixture(scope='session')
def delete_namespace():
    def delete_func(namespace):
        """ Delete an existing namespace """
        helper = KubernetesObjectHelper('v1', 'namespace')
        k8s_obj = helper.get_object(namespace)
        if k8s_obj:
            helper.delete_object(namespace, None, wait=True)
            k8s_obj = helper.get_object(namespace)
        return k8s_obj
    return delete_func


def _get_id(argvalue):
    type = ''
    if argvalue.get('create'):
        type = 'create'
    elif argvalue.get('patch'):
        type = 'patch'
    elif argvalue.get('remove'):
        type = 'remove'
    elif argvalue.get('replace'):
        type = 'replace'
    return type + '_' + argvalue[type]['name'] + '_' + "{:0>3}".format(argvalue['seq'])


def pytest_generate_tests(metafunc):
    _, api_version, resource = metafunc.module.__name__.split('_', 2)
    yaml_name = api_version + '_' + resource + '.yml'
    yaml_path = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                              '../../openshift/ansiblegen/examples', yaml_name))
    if not os.path.exists(yaml_path):
        raise Exception("ansible_data: Unable to locate {}".format(yaml_path))
    with open(yaml_path, 'r') as f:
        data = yaml.load(f)
    seq = 0
    for task in data:
        seq += 1
        task['seq'] = seq

    if 'create_tasks' in metafunc.fixturenames:
        tasks = [x for x in data if x.get('create')]
        metafunc.parametrize("create_tasks", tasks, False, _get_id)
    if 'patch_tasks' in metafunc.fixturenames:
        tasks = [x for x in data if x.get('patch')]
        metafunc.parametrize("patch_tasks", tasks, False, _get_id)
    if 'remove_tasks' in metafunc.fixturenames:
        tasks = [x for x in data if x.get('remove')]
        metafunc.parametrize("remove_tasks", tasks, False, _get_id)
    if 'replace_tasks' in metafunc.fixturenames:
        tasks = [x for x in data if x.get('replace')]
        metafunc.parametrize("replace_tasks", tasks, False, _get_id)
    if 'namespaces' in metafunc.fixturenames:
        tasks = [x for x in data if x.get('create') and x['create'].get('namespace')]
        unique_namespaces = dict()
        for task in tasks:
            unique_namespaces[task['create']['namespace']] = None
        metafunc.parametrize("namespaces", list(unique_namespaces.keys()))
