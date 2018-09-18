import os
import copy
import time
import yaml

import pytest
from pytest_bdd import (
    given,
    then,
    when,
    parsers
)

import kubernetes

from openshift.dynamic import DynamicClient, exceptions


@pytest.fixture
def object_contains():
    def dict_is_subset(obj, subset):
        return all([mapping.get(type(obj[k]), mapping['default'])(obj[k], v) for (k, v) in subset.items()])

    def list_is_subset(obj, subset):
        return all([mapping.get(type(obj[i]), mapping['default'])(obj[i], v) for (i, v) in enumerate(subset)])

    def values_match(obj, subset):
        return obj == subset

    mapping = {
        dict: dict_is_subset,
        list: list_is_subset,
        tuple: list_is_subset,
        'default': values_match
    }

    return dict_is_subset


@pytest.fixture
def definition_loader(group_version, kind):

    def inner(name):
        filename = '_'.join([group_version, kind, name]).replace('/', '_') + '.yaml'
        path = os.path.join(os.path.dirname(__file__), 'definitions', filename)
        with open(path, 'r') as f:
            return yaml.load(f.read())

    return inner


@pytest.fixture
def context():
    state = {}
    return state


@given(parsers.parse('<group_version>.<kind> <name> does not exist in <namespace>'))
def ensure_resource_not_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> does not exist in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    try:
        resource.delete(name, namespace)
    except exceptions.NotFoundError:
        pass


def ensure_resource(resource, body, namespace):
    try:
        return resource.create(body=body, namespace=namespace)
    except exceptions.ConflictError:
        return resource.get(name=body['metadata']['name'], namespace=namespace)
    except exceptions.InternalServerError as e:
        error = yaml.load(e.body)
        retry_after_seconds = error['details'].get('retryAfterSeconds')
        if not retry_after_seconds:
            raise
        time.sleep(retry_after_seconds)
        return resource.create(body=body, namespace=namespace)


@given(parsers.parse('<group_version>.<kind> <name> exists in <namespace>'))
def ensure_resource_in_namespace(admin_client, group_version, kind, name, namespace, definition_loader):
    """<group_version>.<kind> <name> exists in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    instance = ensure_resource(resource, definition_loader(name), namespace)
    assert instance is not None


@given(parsers.parse('I have created <group_version>.<kind> <name> in <namespace>'))
def ensure_user_resource_in_namespace(client, group_version, kind, name, namespace, definition_loader):
    """<group_version>.<kind> <name> exists in <namespace>."""
    resource = client.resources.get(api_version=group_version, kind=kind)
    instance = ensure_resource(resource, definition_loader(name), namespace)
    assert instance is not None


@when(parsers.parse('I {action} <group_version>.<kind> <name> in <namespace>'))
def perform_action_in_namespace(context, client, action, group_version, kind, name, namespace):
    """I <action> <group_version>_<kind>_<namespace>_<name>.yaml."""
    fail = not action.startswith('try to ')
    action = action.replace('try to ', '')
    resource = client.resources.get(api_version=group_version, kind=kind)
    try:
        if action == 'create':
            context["instance"] = resource.create(body=definition_loader(name), namespace=namespace)
        elif action == 'delete':
            context["instance"] = resource.delete(name=name, namespace=namespace)
        elif action == 'get':
            context["instance"] = resource.get(name=name, namespace=namespace)
        else:
            raise ValueError("Unable to {action} resource!".format(action))
    except Exception as e:
        context['exc'] = e
        if fail:
            raise


@then(parsers.parse('It throws a {error}'))
def it_throws_an_error(context, error):
    """It throws an error"""
    assert isinstance(context['exc'], getattr(exceptions, error))


@given(parsers.parse('I have {clusterrole} permissions in <namespace>'))
def client(clusterrole, namespace, kubeconfig, port, admin_client):
    """I have <clusterrole> permissions in <namespace>."""
    needs_admin = namespace == 'all namespaces'
    if needs_admin:
        return admin_client

    k8s_client = kubernetes.config.new_client_from_config(str(kubeconfig))
    # k8s_client.configuration.verify_ssl = False
    k8s_client.configuration.host = 'https://localhost:{}'.format(port)

    v1_tkr = admin_client.resources.get(api_version='authentication.k8s.io/v1', kind='TokenReview')

    username = v1_tkr.create({
        "apiVersion": "authentication.k8s.io/v1",
        "kind": "TokenReview",
        "spec": {
            "token": k8s_client.configuration.api_key['authorization'].replace('Bearer ', '')
        }
    }).status.user.username

    v1_projects = admin_client.resources.get(api_version='project.openshift.io/v1', kind="Project")
    try:
        v1_projects.create({"apiVersion": "project.openshift.io/v1", "kind": "Project", "metadata": {"name": namespace}})
    except exceptions.ConflictError:
        pass

    role_binding = {
        "kind": "RoleBinding",
        "apiVersion": "rbac.authorization.k8s.io/v1",
        "metadata": {
            "name": "{}-{}".format(username, clusterrole),
            "namespace": namespace,
        },
        "roleRef": {
            "kind": "ClusterRole",
            "name": clusterrole,
            "apiGroup": "rbac.authorization.k8s.io",
        },
        "subjects": [{
            "kind": "User",
            "name": username,
            "apiGroup": "rbac.authorization.k8s.io",
        }]
    }
    rbs = admin_client.resources.get(kind='RoleBinding', api_version='rbac.authorization.k8s.io/v1')
    try:
        rbs.create(role_binding)
    except exceptions.ConflictError:
        pass

    return DynamicClient(k8s_client)
