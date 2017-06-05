# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy

import pytest

from openshift.helper.exceptions import OpenShiftException


@pytest.fixture()
def create_params(create_tasks, project, object_name):
    parameters = create_tasks['create']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def patch_params(patch_tasks, project, object_name):
    parameters = patch_tasks['patch']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def replace_params(replace_tasks, project, object_name):
    parameters = replace_tasks['replace']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def stateful_set(ansible_helper, create_params):
    ansible_helper.api_version = 'apps/v1beta1'
    request_body = ansible_helper.request_body_from_params(create_params)
    namespace = create_params.get('namespace')
    name = create_params.get('name')
    k8s_obj = ansible_helper.create_object(namespace, body=request_body)

    yield k8s_obj

    try:
        ansible_helper.delete_object(name, namespace)
    except OpenShiftException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404:
            raise


def test_create_stateful_set(ansible_helper, create_params, stateful_set, obj_compare):
    ansible_helper.api_version = 'apps/v1beta1'
    obj_compare(ansible_helper, stateful_set, create_params)


def test_get_stateful_set(ansible_helper, stateful_set):
    ansible_helper.api_version = 'apps/v1beta1'
    name = stateful_set.metadata.name
    namespace = stateful_set.metadata.namespace
    k8s_obj = ansible_helper.get_object(name, namespace)
    assert k8s_obj is not None


def test_patch_stateful_set(ansible_helper, stateful_set, patch_params, obj_compare):
    ansible_helper.api_version = 'apps/v1beta1'
    name = patch_params.get('name')
    namespace = patch_params.get('namespace')
    existing_obj = stateful_set
    updated_obj = copy.deepcopy(existing_obj)
    ansible_helper.object_from_params(patch_params, obj=updated_obj)
    match, _ = ansible_helper.objects_match(existing_obj, updated_obj)
    assert not match
    new_obj = ansible_helper.patch_object(name, namespace, updated_obj)
    assert new_obj is not None
    obj_compare(ansible_helper, new_obj, patch_params)


def test_replace_stateful_set(ansible_helper, stateful_set, replace_params, obj_compare):
    ansible_helper.api_version = 'apps/v1beta1'
    name = replace_params.get('name')
    namespace = replace_params.get('namespace')
    existing = stateful_set
    request_body = ansible_helper.request_body_from_params(replace_params)
    k8s_obj = ansible_helper.replace_object(name, namespace, body=request_body)
    obj_compare(ansible_helper, k8s_obj, replace_params)


def test_remove_stateful_set(ansible_helper, stateful_set):
    ansible_helper.api_version = 'apps/v1beta1'
    name = stateful_set.metadata.name
    namespace = stateful_set.metadata.namespace
    ansible_helper.delete_object(name, namespace)
    k8s_obj = ansible_helper.get_object(name, namespace)
    assert k8s_obj is None
