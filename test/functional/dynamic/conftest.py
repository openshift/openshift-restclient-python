import os
import yaml
import time

import pytest
from pytest_bdd import (
    given,
    then,
    when,
    parsers
)

import kubernetes

from openshift.dynamic import DynamicClient, exceptions


def get_definition(group_version, kind, name):
    filename = '_'.join([group_version, kind, name]).replace('/', '_') + '.yaml'
    path = os.path.join(os.path.dirname(__file__), 'definitions', filename)
    with open(path, 'r') as f:
        return yaml.load(f.read())


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


@given(parsers.parse('<group_version>.<kind> <name> exists in <namespace>'))
def ensure_resource_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> exists in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    try:
        instance = resource.get(name, namespace)
    except exceptions.NotFoundError:
        instance = resource.create(body=get_definition(group_version, kind, name), namespace=namespace)
    assert instance is not None


@then(parsers.parse('<group_version>.<kind> <name> exists in <namespace>'))
def resource_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> exists in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    instance = resource.get(name, namespace)
    assert instance.metadata.name == name
    assert instance.metadata.namespace == namespace


@then(parsers.parse('<group_version>.<kind> <name> does not exist in <namespace>'))
def resource_not_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> does not exist in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    with pytest.raises(exceptions.NotFoundError):
        resource.get(name, namespace)



@when(parsers.parse('I {action} <group_version>.<kind> <name> in <namespace>'))
def perform_action_in_namespace(context, client, action, group_version, kind, name, namespace):
    """I <action> <group_version>_<kind>_<namespace>_<name>.yaml."""
    fail = not action.startswith('try to ')
    action = action.replace('try to ', '')
    resource = client.resources.get(api_version=group_version, kind=kind)
    try:
        if action == 'create':
            context["instance"] = resource.create(body=get_definition(group_version, kind, name), namespace=namespace)
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

    v1_namespaces = admin_client.resources.get(api_version='v1', kind="Namespace")
    try:
        v1_namespaces.create({"apiVersion": "v1", "kind": "Namespace", "metadata": {"name": namespace}})
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
        # TODO(fabianvf): Determine why this role doesn't take effect immediately
        time.sleep(5)
    except exceptions.ConflictError:
        pass

    return DynamicClient(k8s_client)
