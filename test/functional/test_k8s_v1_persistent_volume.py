# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import pytest

from openshift.helper.exceptions import KubernetesException

# TODO: Because of the way tests are run, pvs will always time out.
#       need to find a way to mock this out better
@pytest.fixture()
def host_dir(tmpdir_factory):
    host_dir = tmpdir_factory.mktemp('volume')
    return host_dir.strpath


@pytest.fixture()
def create_params(create_tasks, project, object_name, host_dir):
    parameters = create_tasks['create']
    parameters.update({
        "name": object_name,
        "capacity": {
            'storage': '1Gi',
        },
        "access_modes": ['ReadWriteOnce'],
        "persistent_volume_reclaim_policy": 'Recycle',
        "host_path_path": host_dir
    })
    return parameters


@pytest.fixture()
def patch_params(patch_tasks, project, object_name):
    parameters = patch_tasks['patch']
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def replace_params(replace_tasks, project, object_name):
    parameters = replace_tasks['replace']
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def persistent_volume(admin_k8s_ansible_helper, create_params):
    request_body = admin_k8s_ansible_helper.request_body_from_params(create_params)
    name = create_params.get('name')
    k8s_obj = admin_k8s_ansible_helper.create_object(None, body=request_body)

    yield k8s_obj

    try:
        admin_k8s_ansible_helper.delete_object(name, None)
    except KubernetesException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404 and ex.value.get('status') != 403:
            raise


def test_create_persistent_volume(admin_k8s_ansible_helper, create_params, persistent_volume, obj_compare):
    obj_compare(admin_k8s_ansible_helper, persistent_volume, create_params)


def test_get_persistent_volume(admin_k8s_ansible_helper, persistent_volume):
    name = persistent_volume.metadata.name
    k8s_obj = admin_k8s_ansible_helper.get_object(name, None)
    assert k8s_obj is not None


def test_remove_persistent_volume(admin_k8s_ansible_helper, persistent_volume):
    name = persistent_volume.metadata.name
    admin_k8s_ansible_helper.delete_object(name, None)
    k8s_obj = admin_k8s_ansible_helper.get_object(name, None)
    assert k8s_obj is None
