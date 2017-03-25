# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import pytest

from openshift.helper.exceptions import KubernetesException


# TODO: Because of the way tests are run, pvcs will always time out.
#       need to find a way to mock this out better
@pytest.fixture()
def create_params(create_tasks, project, object_name):
    parameters = create_tasks['create']
    parameters.update({
        "name": object_name,
        "namespace": project,
        "access_modes": ['ReadWriteOnce'],
        "resources_requests": {
            "storage": "1Gi"
        }
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
def persistent_volume_claim(k8s_ansible_helper, create_params):
    request_body = k8s_ansible_helper.request_body_from_params(create_params)
    name = create_params.get('name')
    namespace = create_params.get('namespace')
    k8s_obj = k8s_ansible_helper.create_object(namespace, body=request_body)

    yield k8s_obj

    try:
        k8s_ansible_helper.delete_object(name, namespace)
    except KubernetesException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404 and ex.value.get('status') != 403:
            raise


def test_create_persistent_volume_claim(k8s_ansible_helper, create_params, persistent_volume_claim, obj_compare):
    obj_compare(k8s_ansible_helper, persistent_volume_claim, create_params)


def test_get_persistent_volume_claim(k8s_ansible_helper, persistent_volume_claim):
    name = persistent_volume_claim.metadata.name
    namespace = persistent_volume_claim.metadata.namespace
    k8s_obj = k8s_ansible_helper.get_object(name, namespace)
    assert k8s_obj is not None


def test_remove_persistent_volume_claim(k8s_ansible_helper, persistent_volume_claim):
    name = persistent_volume_claim.metadata.name
    namespace = persistent_volume_claim.metadata.namespace
    k8s_ansible_helper.delete_object(name, namespace)
    k8s_obj = k8s_ansible_helper.get_object(name, namespace)
    assert k8s_obj is None
