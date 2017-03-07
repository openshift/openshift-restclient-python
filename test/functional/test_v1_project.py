# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy


def test_create_project(ansible_helper, create_tasks, obj_compare, create_namespace):
    parameters = create_tasks['create']
    new_obj = ansible_helper.object_from_params(parameters)
    namespace = parameters.get('namespace')
    if namespace:
        create_namespace(namespace)
    k8s_obj = ansible_helper.create_object(namespace, new_obj, wait=True)
    obj_compare(ansible_helper, k8s_obj, parameters)


def test_get_project(ansible_helper, create_tasks):
    parameters = create_tasks['create']
    namespace = parameters.get('namespace')
    k8s_obj = ansible_helper.get_object(parameters['name'], namespace)
    assert k8s_obj is not None


def test_project_idempotence(ansible_helper, create_tasks):
    parameters = create_tasks['create']
    namespace = parameters.get('namespace')
    k8s_obj = ansible_helper.get_object(parameters['name'], namespace)
    updated_obj = copy.deepcopy(k8s_obj)
    ansible_helper.object_from_params(parameters, obj=updated_obj)
    assert ansible_helper.objects_match(k8s_obj, updated_obj)


def test_patch_project(ansible_helper, patch_tasks, obj_compare):
    parameters = patch_tasks['patch']
    namespace = parameters.get('namespace')
    existing_obj = ansible_helper.get_object(parameters['name'], namespace)
    updated_obj = copy.deepcopy(existing_obj)
    ansible_helper.object_from_params(parameters, obj=updated_obj)
    match = ansible_helper.objects_match(existing_obj, updated_obj)
    assert not match
    new_obj = ansible_helper.patch_object(parameters['name'], namespace, updated_obj, wait=True)
    assert new_obj is not None
    obj_compare(ansible_helper, new_obj, parameters)


def test_remove_service(ansible_helper, create_tasks):
    parameters = create_tasks['create']
    namespace = parameters.get('namespace')
    ansible_helper.delete_object(parameters['name'], namespace, wait=True)
    k8s_obj = ansible_helper.get_object(parameters['name'], namespace)
    assert k8s_obj is None


def test_remove_namespace(namespaces, delete_namespace):
    k8s_obj = delete_namespace(namespaces)
    assert k8s_obj is None
