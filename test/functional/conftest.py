# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import re
import io
import os
import copy
import time
import uuid
import yaml
import socket
import tarfile
from contextlib import closing

import json
import docker
import pytest
import requests

from pkg_resources import parse_version

from openshift.client import models
from kubernetes.client import V1Namespace, V1ObjectMeta
from openshift.helper.ansible import KubernetesAnsibleModuleHelper, OpenShiftAnsibleModuleHelper

if os.path.exists(os.path.join(os.getcwd(), 'KubeObjHelper.log')):
    os.remove(os.path.join(os.getcwd(), 'KubeObjHelper.log'))



@pytest.fixture(scope='session')
def port():
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        return s.getsockname()[1]


@pytest.fixture(scope='session')
def openshift_container(request, port, pytestconfig):
    capmanager = pytestconfig.pluginmanager.getplugin('capturemanager')
    client = docker.from_env()
    openshift_version = request.config.getoption('--openshift-version')
    if openshift_version is None:
        yield None
    else:
        container = client.containers.run(
            'openshift/origin:{}'.format(openshift_version),
            'start master --listen=0.0.0.0:{}'.format(port),
            detach=True,
            ports={port: port}
        )

        try:
            # Wait for the container to no longer be in the created state before
            # continuing
            while container.status == u'created':
                capmanager.suspendcapture()
                print("\nWaiting for container...")
                capmanager.resumecapture()
                time.sleep(5)
                container = client.containers.get(container.id)

            # Wait for the api server to be ready before continuing
            for _ in range(10):
                try:
                    requests.head("https://127.0.0.1:{}/healthz/ready".format(port), verify=False)
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


def parse_test_name(name):
    pieces = re.findall('[A-Z][a-z0-9]*', name)
    cluster_type = pieces[1].lower()
    api_version = pieces[2].lower()
    resource = '_'.join(map(str.lower, pieces[3:]))
    return cluster_type, api_version, resource


@pytest.fixture(scope='class')
def ansible_helper(request, auth):
    cluster_type, api_version, resource = parse_test_name(request.node.name)
    if cluster_type == 'k8s':
        helper = KubernetesAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)
    else:
        helper = OpenShiftAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)

    helper.api_client.configuration.debug = True

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
        ansible_helper.log(k8s_obj.to_str())
        ansible_helper.log('\n\n')

        ansible_helper.log('from params:')
        ansible_helper.log(requested.to_str())
        ansible_helper.log('\n\n')

        match, diff = ansible_helper.objects_match(k8s_obj, requested)
        if not match:
            ansible_helper.log('\n\n')
            ansible_helper.log('Differences:')
            ansible_helper.log(json.dumps(diff, indent=4))
            ansible_helper.log('\n\n')
        assert match

    return compare_func


@pytest.fixture(scope='class')
def namespace(auth):
    name = "test-{}".format(uuid.uuid4())

    helper = KubernetesAnsibleModuleHelper('v1', 'namespace', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_object(V1Namespace(metadata=V1ObjectMeta(name=name)))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


@pytest.fixture()
def object_name(request):
    action = request.function.__name__.split('_')[1]
    return '{}-{}'.format(action, uuid.uuid4())[:22].strip('-')

@pytest.fixture(scope='class')
def auth(request, kubeconfig, admin_kubeconfig, port):
    # needs_admin = request.node.cls.tasks.get('admin')
    needs_admin = True
    config = admin_kubeconfig if needs_admin else kubeconfig
    if config is not None:
        return {
            'kubeconfig': str(config),
            'host': 'https://localhost:{}'.format(port),
            'verify_ssl': False
        }

    return {}


@pytest.fixture(scope='class')
def project(auth):
    name = "test-{}".format(uuid.uuid4())
    helper = OpenShiftAnsibleModuleHelper('v1', 'project', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_project(metadata=V1ObjectMeta(name=name))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


@pytest.fixture
def openshift_version():
    return pytest.config.getoption('--openshift-version')


@pytest.fixture(autouse=True)
def skip_empty(request):
    _, api_version, resource = parse_test_name(request.node.cls._type)
    action = request.function.__name__.split('_')[1]
    tasks = list(filter(lambda x: x.get(action), request.node.cls.tasks['tasks']))
    if not tasks and action not in ['get', 'remove']:
        pytest.skip('No example provided to {} {}'.format(action, resource))


@pytest.fixture(autouse=True)
def skip_by_version(request, openshift_version):
    if request.node.cls.tasks.get('version_limits') and openshift_version:
        lowest_version = request.node.cls.tasks['version_limits'].get('min')
        highest_version = request.node.cls.tasks['version_limits'].get('max')
        skip_latest = request.node.cls.tasks['version_limits'].get('skip_latest')

        too_low = lowest_version and parse_version(lowest_version) > parse_version(openshift_version)
        too_high = highest_version and parse_version(highest_version) < parse_version(openshift_version)

        if openshift_version == 'latest':
            if skip_latest:
                pytest.skip('This API is not supported in the latest openshift version')
        elif too_low:
            pytest.skip('This API is not supported in openshift versions > {}. You are using version {}'.format(lowest_version, openshift_version))
        elif too_high:
            pytest.skip('This API is not supported in openshift versions < {}. You are using version {}'.format(highest_version, openshift_version))


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
