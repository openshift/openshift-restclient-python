import os
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

from openshift.dynamic import DynamicClient, ResourceList, exceptions


def object_contains(obj, subset):
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

    return dict_is_subset(obj, subset)


def load_definition(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as f:
        return yaml.load(f.read())


@pytest.fixture
def definition(filename):
    return load_definition(filename)


@pytest.fixture
def context():
    state = {}
    return state


def ensure_resource(resource, body, namespace):
    try:
        return resource.create(body=body, namespace=namespace)
    except exceptions.ConflictError:
        if isinstance(resource, ResourceList):
            return resource.get(body=body, namespace=namespace)
        return resource.get(name=body['metadata']['name'], namespace=namespace)
    except exceptions.InternalServerError as e:
        error = yaml.load(e.body)
        retry_after_seconds = error['details'].get('retryAfterSeconds')
        if not retry_after_seconds:
            raise
        time.sleep(retry_after_seconds)
        return resource.create(body=body, namespace=namespace)
    except Exception:
        #  TODO: Sometimes we hit a timing issue, for now I'll just sleep
        time.sleep(3)
        return resource.create(body=body, namespace=namespace)


@given(parsers.parse('The content of <filename> does not exist in <namespace>'))
def ensure_resource_not_in_namespace(admin_client, namespace, definition):
    resource = admin_client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    try:
        if isinstance(resource, ResourceList):
            resource.delete(body=definition, namespace=namespace)
        else:
            resource.delete(definition['metadata']['name'], namespace)
    except exceptions.NotFoundError:
        pass


@given(parsers.parse('The content of <filename> exists in <namespace>'))
def ensure_resource_in_namespace(admin_client, namespace, definition):
    resource = admin_client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    instance = ensure_resource(resource, definition, namespace)
    assert instance is not None


@given(parsers.parse('I have created <filename> in <namespace>'))
def ensure_user_resource_in_namespace(client, namespace, definition):
    """I have created <filename> in <namespace>."""
    resource = client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    instance = ensure_resource(resource, definition, namespace)
    assert instance is not None


def ensure_namespace(admin_client, namespace):
    v1_projects = admin_client.resources.get(api_version='project.openshift.io/v1', kind="Project")
    try:
        project = v1_projects.get(name=namespace)
    except exceptions.NotFoundError:
        project = v1_projects.create({"apiVersion": "project.openshift.io/v1", "kind": "Project", "metadata": {"name": namespace}})
    if project.metadata.DeletionTimestamp:
        # Wait up to 5 minutes for project to terminate
        for _ in range(300):
            try:
                project = v1_projects.get(name=namespace)
            except exceptions.NotFoundError:
                project = v1_projects.create({"apiVersion": "project.openshift.io/v1", "kind": "Project", "metadata": {"name": namespace}})
                return project
    return project



@given(parsers.parse('I have {clusterrole} permissions in <namespace>'))
def client(clusterrole, namespace, kubeconfig, port, admin_client):
    """I have <clusterrole> permissions in <namespace>."""
    needs_admin = namespace == 'all namespaces'
    if needs_admin:
        return admin_client

    ensure_namespace(admin_client, namespace)

    k8s_client = kubernetes.config.new_client_from_config(str(kubeconfig))
    k8s_client.configuration.host = 'https://localhost:{}'.format(port)

    v1_tkr = admin_client.resources.get(api_version='authentication.k8s.io/v1', kind='TokenReview')

    username = v1_tkr.create({
        "apiVersion": "authentication.k8s.io/v1",
        "kind": "TokenReview",
        "spec": {
            "token": k8s_client.configuration.api_key['authorization'].replace('Bearer ', '')
        }
    }).status.user.username


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


@when(parsers.parse('I {action} <filename> with <update> in <namespace>'))
def perform_update_action_in_namespace(context, client, action, namespace, definition, update):

    def set_resource_version(r, resource):
        try:
            r['metadata']['resourceVersion'] = resource.get(r['metadata']['name'], namespace=namespace).metadata.resourceVersion
        except exceptions.NotFoundError:
            r['metadata']['resourceVersion'] = "0"
        return r

    fail = not action.startswith('try to ')
    action = action.replace('try to ', '')
    resource = client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    try:
        if action == 'replace':
            replace = load_definition(update)
            if isinstance(resource, ResourceList):
                replace['items'] = [set_resource_version(item, resource.resource) for item in replace['items']]
            else:
                replace = set_resource_version(replace, resource)
            context['instance'] = resource.replace(body=replace, namespace=namespace)
        elif action == 'patch':
            patch = load_definition(update)
            context['instance'] = resource.patch(body=patch, namespace=namespace)
        else:
            fail = True
            raise ValueError('Unable to {action} resource!'.format(action))
    except Exception as e:
        context['exc'] = e
        if fail:
            raise


@when(parsers.parse('I {action} <filename> in <namespace>'))
def perform_action_in_namespace(context, client, action, namespace, definition):
    fail = not action.startswith('try to ')
    action = action.replace('try to ', '')
    resource = client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    try:
        if action == 'create':
            context['instance'] = resource.create(body=definition, namespace=namespace)
        elif action == 'delete':
            if isinstance(resource, ResourceList):
                context['instance'] = resource.delete(body=definition, namespace=namespace)
            else:
                context['instance'] = resource.delete(name=definition['metadata']['name'], namespace=namespace)
        elif action == 'get':
            if isinstance(resource, ResourceList):
                context['instance'] = resource.get(body=definition, namespace=namespace)
            else:
                context['instance'] = resource.get(name=definition['metadata']['name'], namespace=namespace)
        else:
            fail = True
            raise ValueError('Unable to {action} resource!'.format(action))
    except Exception as e:
        context['exc'] = e
        if fail:
            raise


@then(parsers.parse('It throws a {error}'))
def it_throws_an_error(context, error):
    """It throws an error"""
    assert isinstance(context['exc'], getattr(exceptions, error))


@then('The resources in <filename> in <namespace> should match the content of <update>')
def resource_should_match_update(admin_client, namespace, update, definition):
    update = load_definition(update)
    resource = admin_client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    if isinstance(resource, ResourceList):
        cluster_instance = resource.get(body=definition, namespace=namespace).to_dict()
    else:
        cluster_instance = resource.get(name=definition['metadata']['name'], namespace=namespace).to_dict()
    assert object_contains(cluster_instance, update)


@then(parsers.parse('The content of <filename> does not exist in <namespace>'))
def resource_not_in_namespace(admin_client, namespace, definition):

    def assert_resource_does_not_exist(resource, resource_definition, namespace):
        with pytest.raises(exceptions.NotFoundError):
            resource.get(resource_definition['metadata']['name'], namespace)

    resource = admin_client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    if isinstance(resource, ResourceList):
        for item in definition['items']:
            assert_resource_does_not_exist(resource.resource, item, namespace)
    else:
        assert_resource_does_not_exist(resource, definition, namespace)


@then(parsers.parse('The content of <filename> exists in <namespace>'))
def resource_in_namespace(admin_client, namespace, definition):

    def assert_resource_exists(resource, resource_definition, namespace):
        instance = resource.get(resource_definition['metadata']['name'], namespace)
        assert instance.metadata.name == resource_definition['metadata']['name']
        assert instance.metadata.namespace == namespace

    resource = admin_client.resources.get(api_version=definition['apiVersion'], kind=definition['kind'])
    if isinstance(resource, ResourceList):
        for item in definition['items']:
            assert_resource_exists(resource.resource, item, namespace)
    else:
        assert_resource_exists(resource, definition, namespace)
