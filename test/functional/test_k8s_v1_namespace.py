# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy

import pytest

from openshift.helper.exceptions import KubernetesException


@pytest.fixture()
def create_params(create_tasks, object_name):
    parameters = create_tasks['create']
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def patch_params(patch_tasks, object_name):
    parameters = patch_tasks['patch']
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def replace_params(replace_tasks, object_name):
    parameters = replace_tasks['replace']
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def k8s_namespace(admin_k8s_ansible_helper, create_params):
    request_body = admin_k8s_ansible_helper.request_body_from_params(create_params)
    name = create_params.get('name')
    k8s_obj = admin_k8s_ansible_helper.create_object(None, body=request_body)

    yield k8s_obj

    try:
        admin_k8s_ansible_helper.delete_object(name, None)
    except KubernetesException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404:
            raise


def test_create_namespace(admin_k8s_ansible_helper, create_params, k8s_namespace, obj_compare):
    obj_compare(admin_k8s_ansible_helper, k8s_namespace, create_params)


def test_get_namespace(admin_k8s_ansible_helper, k8s_namespace):
    name = k8s_namespace.metadata.name
    k8s_obj = admin_k8s_ansible_helper.get_object(name, None)
    assert k8s_obj is not None


def test_patch_namespace(admin_k8s_ansible_helper, k8s_namespace, patch_params, obj_compare):
    name = patch_params.get('name')
    existing_obj = k8s_namespace
    updated_obj = copy.deepcopy(existing_obj)
    admin_k8s_ansible_helper.object_from_params(patch_params, obj=updated_obj)
    match, _ = admin_k8s_ansible_helper.objects_match(existing_obj, updated_obj)
    assert not match
    new_obj = admin_k8s_ansible_helper.patch_object(name, None, updated_obj)
    assert new_obj is not None
    obj_compare(admin_k8s_ansible_helper, new_obj, patch_params)


def test_replace_namespace(admin_k8s_ansible_helper, k8s_namespace, replace_params, obj_compare):
    name = replace_params.get('name')
    request_body = admin_k8s_ansible_helper.request_body_from_params(replace_params)
    k8s_obj = admin_k8s_ansible_helper.replace_object(name, None, body=request_body)
    obj_compare(admin_k8s_ansible_helper, k8s_obj, replace_params)


def test_remove_namespace(admin_k8s_ansible_helper, k8s_namespace):
    name = k8s_namespace.metadata.name
    admin_k8s_ansible_helper.delete_object(name, None)
    k8s_obj = admin_k8s_ansible_helper.get_object(name, None)
    assert k8s_obj is None
