# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import pytest

from openshift.helper.exceptions import OpenShiftException


@pytest.fixture()
def create_params(create_tasks, object_name):
    parameters = create_tasks['create']
    parameters['namespace'] = None
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def patch_params(patch_tasks, object_name):
    parameters = patch_tasks['patch']
    parameters['namespace'] = None
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def replace_params(replace_tasks, object_name):
    parameters = replace_tasks['replace']
    parameters['namespace'] = None
    parameters['name'] = object_name
    return parameters


@pytest.fixture()
def openshift_project(openshift_ansible_helper, create_params):
    new_obj = openshift_ansible_helper.object_from_params(create_params)
    name = create_params.get('name')
    k8s_obj = openshift_ansible_helper.create_project(metadata=new_obj.metadata)

    yield k8s_obj

    try:
        openshift_ansible_helper.delete_object(name, None)
    except OpenShiftException as ex:
        # Swallow exception if object is already removed
        if ex.value.get('status') != 404 and ex.value.get('status') != 403:
            raise


def test_create_project(openshift_ansible_helper, create_params, openshift_project, obj_compare):
    obj_compare(openshift_ansible_helper, openshift_project, create_params)


def test_create_duplicate_project(openshift_ansible_helper, create_params, openshift_project, obj_compare):
    with pytest.raises(OpenShiftException):
        obj_compare(openshift_ansible_helper, openshift_project, create_params)


def test_get_project(openshift_ansible_helper, openshift_project):
    name = openshift_project.metadata.name
    k8s_obj = openshift_ansible_helper.get_object(name, None)
    assert k8s_obj is not None


def test_remove_project(openshift_ansible_helper, openshift_project):
    name = openshift_project.metadata.name
    openshift_ansible_helper.delete_object(name, None)
    k8s_obj = openshift_ansible_helper.get_object(name, None)
    assert k8s_obj is None
