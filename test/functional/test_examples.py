# -**-
from __future__ import absolute_import
from __future__ import print_function

import os
import copy

import yaml

import pytest

from openshift.helper.ansible import OpenShiftAnsibleModuleHelper, KubernetesAnsibleModuleHelper
from openshift.helper.exceptions import KubernetesException


def get_tasks():
    """ Goes to the examples for the ansible docs and parses out tasks, resources and api versions """
    tasks = []
    example_dir = os.path.normpath(os.path.join(
        os.path.dirname(__file__), '../../openshift/ansiblegen/examples/')
    )
    yaml_names = os.listdir(example_dir)
    for yaml_name in yaml_names:
        cluster, api_version, resource = yaml_name.split('_', 2)
        resource = resource[0:-4]
        yaml_path = os.path.join(example_dir, yaml_name)

        with open(yaml_path, 'r') as f:
            data = yaml.load(f)

        tasks.append(((cluster, api_version, resource), data))
    return tasks


class Example(object):
    """ Contains the logic for testing create/get/patch/replace/remove on an openshift/k8s resource """

    def test_create(self, ansible_helper, create_params, project, object_name, resources, obj_compare):
        for params, resource in zip(create_params, resources):
            obj_compare(ansible_helper, resource, params)

    def test_get(self, ansible_helper, resources):
        for resource in resources:
            name = resource.metadata.name
            namespace = resource.metadata.namespace
            k8s_obj = ansible_helper.get_object(name, namespace)
            assert k8s_obj is not None

    def test_patch_resource(self, ansible_helper, resources, patch_params, obj_compare):
        for i, resource in enumerate(resources):
            for params in patch_params:
                params['name'] = params['name'] + str(i)
                name = params.get('name')
                namespace = params.get('namespace')
                existing_obj = resource
                updated_obj = copy.deepcopy(existing_obj)
                ansible_helper.object_from_params(params, obj=updated_obj)
                match, _ = ansible_helper.objects_match(existing_obj, updated_obj)
                assert not match

                new_obj = ansible_helper.patch_object(name, namespace, updated_obj)
                assert new_obj is not None
                obj_compare(ansible_helper, new_obj, params)
            break

    def test_replace_resource(self, ansible_helper, resources, replace_params, obj_compare):
        for i, resource in enumerate(resources):
            for params in replace_params:
                params['name'] = params['name'] + str(i)
                name = params.get('name')
                namespace = params.get('namespace')
                existing = resource
                request_body = ansible_helper.request_body_from_params(params)
                if hasattr(existing.spec, 'cluster_ip'):
                    # can't change the cluster_ip value
                    request_body['spec']['clusterIP'] = existing.spec.cluster_ip
                k8s_obj = ansible_helper.replace_object(name, namespace, body=request_body)
                obj_compare(ansible_helper, k8s_obj, params)
            break

    def test_remove_resource(self, ansible_helper, resources):
        for resource in resources:
            name = resource.metadata.name
            namespace = resource.metadata.namespace
            ansible_helper.delete_object(name, namespace)
            k8s_obj = ansible_helper.get_object(name, namespace)
            while k8s_obj:
                k8s_obj = ansible_helper.get_object(name, namespace)
            assert k8s_obj is None

    @pytest.fixture()
    def create_params(self, project, object_name):
        create_tasks = list(filter(lambda x: x.get('create'), self.tasks['tasks']))
        parameters = list(map(lambda x: x['create'], create_tasks))
        for i, parameter in enumerate(parameters):
            if parameter.get('namespace'):
                parameter['namespace'] = project
            parameter['name'] = object_name + str(i)
        return parameters

    @pytest.fixture()
    def patch_params(self, project, object_name):
        patch_tasks = list(filter(lambda x: x.get('patch'), self.tasks['tasks']))
        parameters = list(map(lambda x: x['patch'], patch_tasks))
        for parameter in parameters:
            if parameter.get('namespace'):
                parameter['namespace'] = project
            parameter['name'] = object_name
        return parameters

    @pytest.fixture()
    def replace_params(self, project, object_name):
        replace_tasks = list(filter(lambda x: x.get('replace'), self.tasks['tasks']))
        parameters = list(map(lambda x: x['replace'], replace_tasks))
        for parameter in parameters:
            if parameter.get('namespace'):
                parameter['namespace'] = project
            parameter['name'] = object_name
        return parameters


    @pytest.fixture(scope='class')
    def dependencies(self, project, auth):
        dependencies = []
        for dependency in self.tasks.get('dependencies', []):
            resource_name, params = list(dependency.items())[0]
            api, api_version, kind = resource_name.split('_')
            if api == 'k8s':
                ansible_helper = KubernetesAnsibleModuleHelper(api_version, kind, debug=True, reset_logfile=False, **auth)
            else:
                ansible_helper = OpenShiftAnsibleModuleHelper(api_version, kind, debug=True, reset_logfile=False, **auth)
            if params.get('namespace'):
                params['namespace'] = project
            name = params.get('name')
            request_body = ansible_helper.request_body_from_params(params)
            dependencies.append((name, project, ansible_helper.create_object(project, body=request_body)))
        try:
            yield dependencies
        finally:
            for name, namespace, dependency in dependencies:
                try:
                    ansible_helper.delete_object(name, namespace)
                except KubernetesException:
                    pass

    @pytest.fixture()
    def resources(self, ansible_helper, create_params, dependencies):
        k8s_objs = []
        for create in create_params:
            request_body = ansible_helper.request_body_from_params(create)
            namespace = create.get('namespace')
            name = create.get('name')
            k8s_objs.append((name, namespace, ansible_helper.create_object(namespace, body=request_body)))

        try:
            yield list(map(lambda x: x[2], k8s_objs))
        finally:
            exceptions = []
            for name, namespace, k8s_obj in k8s_objs:
                try:
                    ansible_helper.delete_object(name, namespace)
                except KubernetesException as ex:
                    # Swallow exception if object is already removed
                    if ex.value.get('status') != 404:
                        exceptions.append(ex)
            if exceptions:
                raise exceptions[0]


# BEWARE: Here be disgusting meta-programming hacks
# Basically, for each resource we have examples for, generate a subclass of the Example class
# The type of this subclass will be the resource name
# Then inject that class into globals(), where pytest will be able to pick them up and run them
# If you find a better way to do this, please, please let me know

def ClassFactory(name):
    return type(name, (Example,), {})


for ((cluster_type, apiversion, resource_type), tasks) in get_tasks():
    class_name = 'Test{}{}{}'.format(cluster_type.capitalize(), apiversion.capitalize(), ''.join(map(str.capitalize, resource_type.split('_'))))
    globals()[class_name] = ClassFactory(resource_type)
    globals()[class_name]._type = class_name
    globals()[class_name].tasks = tasks
