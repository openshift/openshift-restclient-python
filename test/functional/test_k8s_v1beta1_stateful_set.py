# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import copy

import pytest

from openshift.helper.exceptions import KubernetesException


@pytest.fixture()
def create_params(create_tasks, project, object_name):
    parameters = create_tasks['create']
    parameters['namespace'] = project
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def stateful_set(k8s_ansible_helper, create_params):
    request_body = k8s_ansible_helper.request_body_from_params(create_params)
    namespace = create_params.get('namespace')
    name = create_params.get('name')
    k8s_obj = k8s_ansible_helper.create_object(namespace, body=request_body)

    yield k8s_obj

    try:
        k8s_ansible_helper.delete_object(name, namespace)
    except KubernetesException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404:
            raise


def test_create_stateful_set(k8s_ansible_helper, create_params, stateful_set, obj_compare):
    obj_compare(k8s_ansible_helper, stateful_set, create_params)


def test_get_stateful_set(k8s_ansible_helper, stateful_set):
    name = stateful_set.metadata.name
    namespace = stateful_set.metadata.namespace
    k8s_obj = k8s_ansible_helper.get_object(name, namespace)
    assert k8s_obj is not None


def test_remove_stateful_set(k8s_ansible_helper, stateful_set):
    name = stateful_set.metadata.name
    namespace = stateful_set.metadata.namespace
    k8s_ansible_helper.delete_object(name, namespace)
    k8s_obj = k8s_ansible_helper.get_object(name, namespace)
    assert k8s_obj is None
