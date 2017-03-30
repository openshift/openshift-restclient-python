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
def deployment_config(openshift_ansible_helper, create_params):
    request_body = openshift_ansible_helper.request_body_from_params(create_params)
    namespace = create_params.get('namespace')
    name = create_params.get('name')
    k8s_obj = openshift_ansible_helper.create_object(namespace, body=request_body)

    yield k8s_obj

    try:
        openshift_ansible_helper.delete_object(name, namespace)
    except OpenShiftException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404:
            raise


def test_create_deployment_config(openshift_ansible_helper, create_params, deployment_config, obj_compare):
    obj_compare(openshift_ansible_helper, deployment_config, create_params)


def test_get_deployment(openshift_ansible_helper, deployment_config):
    name = deployment_config.metadata.name
    namespace = deployment_config.metadata.namespace
    k8s_obj = openshift_ansible_helper.get_object(name, namespace)
    assert k8s_obj is not None


def test_patch_deployment(openshift_ansible_helper, deployment_config, patch_params, obj_compare):
    name = patch_params['name']
    namespace = patch_params.get('namespace')
    existing_obj = deployment_config
    updated_obj = copy.deepcopy(existing_obj)
    openshift_ansible_helper.object_from_params(patch_params, obj=updated_obj)
    match, _ = openshift_ansible_helper.objects_match(existing_obj, updated_obj)
    assert not match
    new_obj = openshift_ansible_helper.patch_object(name, namespace, updated_obj)
    assert new_obj is not None
    obj_compare(openshift_ansible_helper, new_obj, patch_params)


def test_replace_deployment(openshift_ansible_helper, deployment_config, replace_params, obj_compare):
    name = replace_params.get('name')
    namespace = replace_params.get('namespace')
    request_body = openshift_ansible_helper.request_body_from_params(replace_params)
    k8s_obj = openshift_ansible_helper.replace_object(name, namespace, body=request_body)
    obj_compare(openshift_ansible_helper, k8s_obj, replace_params)


def test_remove_deployment(openshift_ansible_helper, deployment_config):
    namespace = deployment_config.metadata.namespace
    name = deployment_config.metadata.name
    openshift_ansible_helper.delete_object(name, namespace)
    k8s_obj = openshift_ansible_helper.get_object(name, namespace)
    assert k8s_obj is None
