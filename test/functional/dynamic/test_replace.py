# coding=utf-8
"""replace feature tests."""

from pytest_bdd import (
    scenario,
    then,
    when,
)

from openshift.dynamic.exceptions import NotFoundError


@scenario('replace.feature', 'Replace a resource that does not exist')
def test_replace_a_resource_that_does_not_exist():
    """replace a resource that does not exist."""
    pass


@scenario('replace.feature', 'Replace a resource that exists')
def test_replace_a_resource_that_exists():
    """replace a resource that exists."""
    pass


@when('I replace <group_version>.<kind> <name> in <namespace> with <update>')
def replace_resource_in_namespace(context, client, group_version, kind, name, namespace, update, definition_loader):
    """I replace <group_version>.<kind> <name> in <namespace> with <update>."""
    replace = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    replace['metadata']['resourceVersion'] = resource.get(replace['metadata']['name'], namespace).metadata.resourceVersion

    context['instance'] = resource.replace(body=replace, namespace=namespace)


@when('I try to replace <group_version>.<kind> <name> in <namespace> with <update>')
def attempt_replace_resource_in_namespace(context, client, group_version, kind, name, namespace, update, definition_loader):
    """I try to replace <group_version>.<kind> <name> in <namespace> with <update>."""
    replace = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    try:
        replace['metadata']['resourceVersion'] = resource.get(replace['metadata']['name'], namespace).metadata.resourceVersion
    except NotFoundError:
        replace['metadata']['resourceVersion'] = "0"
    try:
        context['instance'] = resource.replace(body=replace, namespace=namespace)
    except Exception as e:
        context['exc'] = e


@then('<group_version>.<kind> <name> in <namespace> should match the content of <update>')
def resource_should_match_update(context, client, group_version, kind, name, namespace, update, definition_loader, object_contains):
    """<group_version>.<kind> <name> in <namespace> should match the content of <update>."""
    replace = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    cluster_instance = resource.get(name=name, namespace=namespace).to_dict()
    assert object_contains(cluster_instance, replace)
