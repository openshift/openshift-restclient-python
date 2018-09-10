# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import os
import copy
import time
import socket
import tarfile
import warnings
from contextlib import closing

import json
import docker
import pytest
import requests

from urllib3.exceptions import InsecureRequestWarning

import kubernetes
from openshift.dynamic import DynamicClient


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

            # Disable InsecureRequest warnings because we can't get the cert yet
            warnings.simplefilter('ignore', InsecureRequestWarning)
            # Wait for the api server to be ready before continuing
            for _ in range(10):
                try:
                    requests.head("https://127.0.0.1:{}/healthz/ready".format(port), verify=False)
                except requests.RequestException:
                    pass
                time.sleep(1)
            warnings.simplefilter('default', InsecureRequestWarning)

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


@pytest.fixture
def openshift_version():
    return pytest.config.getoption('--openshift-version')


@pytest.fixture(scope='session')
def admin_client(admin_kubeconfig, port):
    k8s_client = kubernetes.config.new_client_from_config(str(admin_kubeconfig))
    # k8s_client.configuration.verify_ssl = False
    k8s_client.configuration.host = 'https://localhost:{}'.format(port)
    return DynamicClient(k8s_client)
