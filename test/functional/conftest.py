# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy
import io
import os
import tarfile
import time
import uuid
import yaml

import docker
import pytest
import requests
import json

from openshift.client import models
from kubernetes.client import V1Namespace, V1ObjectMeta
from openshift.helper.ansible import KubernetesAnsibleModuleHelper, OpenShiftAnsibleModuleHelper

if os.path.exists(os.path.join(os.getcwd(), 'KubeObjHelper.log')):
    os.remove(os.path.join(os.getcwd(), 'KubeObjHelper.log'))


@pytest.fixture(scope='session')
def openshift_container(request):
    client = docker.from_env()
    # TODO: bind to a random host port
    openshift_version = request.config.getoption('--openshift-version')
    if openshift_version is None:
        yield None
    else:
        image_name = 'openshift/origin:{}'.format(openshift_version)
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
                    requests.head("https://127.0.0.1:8443/healthz/ready", verify=False)
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
    if openshift_container is None:
        return None
    else:
        openshift_container.exec_run('oc login -u test -p test')
        tar_stream, _ = openshift_container.get_archive(
            '/var/lib/origin/openshift.local.config/master/admin.kubeconfig')
        tar_obj = tarfile.open(fileobj=io.BytesIO(tar_stream.read()))
        kubeconfig_contents = tar_obj.extractfile('admin.kubeconfig').read()

        kubeconfig_file = tmpdir_factory.mktemp('kubeconfig').join('admin.kubeconfig')
        kubeconfig_file.write(kubeconfig_contents)
        return kubeconfig_file


@pytest.fixture(scope='session')
def admin_kubeconfig(openshift_container, tmpdir_factory):
    # get_archive returns a stream of the tar archive containing the requested
    # files/directories, so we need use BytesIO as an intermediate step.
    if openshift_container is None:
        return None
    else:
        openshift_container.exec_run('oc login -u system:admin')
        tar_stream, _ = openshift_container.get_archive(
            '/var/lib/origin/openshift.local.config/master/admin.kubeconfig')
        tar_obj = tarfile.open(fileobj=io.BytesIO(tar_stream.read()))
        kubeconfig_contents = tar_obj.extractfile('admin.kubeconfig').read()

        kubeconfig_file = tmpdir_factory.mktemp('kubeconfig').join('admin.kubeconfig')
        kubeconfig_file.write(kubeconfig_contents)
        return kubeconfig_file


@pytest.fixture(scope='module')
def k8s_ansible_helper(request, kubeconfig):
    _, _, api_version, resource = request.module.__name__.split('_', 3)
    auth = {}
    if kubeconfig is not None:
        auth = {
            'kubeconfig': str(kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = KubernetesAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)
    helper.api_client.config.debug = True

    return helper


@pytest.fixture(scope='module')
def openshift_ansible_helper(request, kubeconfig):
    _, _, api_version, resource = request.module.__name__.split('_', 3)
    auth = {}
    if kubeconfig is not None:
        auth = {
            'kubeconfig': str(kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = OpenShiftAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)
    helper.api_client.config.debug = True

    return helper


@pytest.fixture(scope='module')
def admin_k8s_ansible_helper(request, admin_kubeconfig):
    _, _, api_version, resource = request.module.__name__.split('_', 3)
    auth = {}
    if admin_kubeconfig is not None:
        auth = {
            'kubeconfig': str(admin_kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = KubernetesAnsibleModuleHelper(api_version, resource, **auth)
    helper.enable_debug(to_file=False)
    helper.api_client.config.debug = True

    return helper


@pytest.fixture(scope='module')
def admin_openshift_ansible_helper(request, admin_kubeconfig):
    _, _, api_version, resource = request.module.__name__.split('_', 3)
    auth = {}
    if admin_kubeconfig is not None:
        auth = {
            'kubeconfig': str(admin_kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = OpenShiftAnsibleModuleHelper(api_version, resource, **auth)
    helper.enable_debug(to_file=False)
    helper.api_client.config.debug = True

    return helper


@pytest.fixture(scope='session')
def obj_compare():
    def compare_func(ansible_helper, k8s_obj, parameters):
        """ Assert that an object matches an expected object """
        requested = copy.deepcopy(k8s_obj)
        ansible_helper.object_from_params(parameters, obj=requested)

        ansible_helper.log('paramters:')
        ansible_helper.log(json.dumps(parameters, indent=4))
        ansible_helper.log('\n\n')

        ansible_helper.log('k8s_obj:')
        ansible_helper.log(json.dumps(k8s_obj.to_dict(), indent=4))
        ansible_helper.log('\n\n')

        ansible_helper.log('from params:')
        ansible_helper.log(json.dumps(requested.to_dict(), indent=4))
        ansible_helper.log('\n\n')

        match, diff = ansible_helper.objects_match(k8s_obj, requested)
        if not match:
            ansible_helper.log('\n\n')
            ansible_helper.log('Differences:')
            ansible_helper.log(json.dumps(diff, indent=4))
            ansible_helper.log('\n\n')
        assert match

    return compare_func


@pytest.fixture(scope='module')
def namespace(kubeconfig):
    name = "test-{}".format(uuid.uuid4())

    auth = {}
    if kubeconfig is not None:
        auth = {
            'kubeconfig': str(kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = KubernetesAnsibleModuleHelper('v1', 'namespace', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_object(V1Namespace(metadata=V1ObjectMeta(name=name)))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


@pytest.fixture()
def object_name():
    # v1.3 services cannot be longer than 24 characters long
    # truncate at 23 to avoid a trailing '-'
    name = 'test-{}'.format(uuid.uuid4())[:23]
    return name


@pytest.fixture(scope='module')
def project(kubeconfig):
    name = "test-{}".format(uuid.uuid4())
    auth = {}
    if kubeconfig is not None:
        auth = {
            'kubeconfig': str(kubeconfig),
            'host': 'https://localhost:8443',
            'verify_ssl': False
        }
    helper = OpenShiftAnsibleModuleHelper('v1', 'project', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_project(metadata=V1ObjectMeta(name=name))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


def _get_id(argvalue):
    op_type = ''
    if argvalue.get('create'):
        op_type = 'create'
    elif argvalue.get('patch'):
        op_type = 'patch'
    elif argvalue.get('remove'):
        op_type = 'remove'
    elif argvalue.get('replace'):
        op_type = 'replace'
    return op_type + '_' + argvalue[op_type]['name'] + '_' + "{:0>3}".format(argvalue['seq'])


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
