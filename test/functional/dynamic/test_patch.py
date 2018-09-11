# coding=utf-8
"""Patch feature tests."""

from pytest_bdd import (
    scenario,
    then,
    when,
)


@scenario('patch.feature', 'Patch a resource that does not exist')
def test_patch_a_resource_that_does_not_exist():
    """Patch a resource that does not exist."""
    pass


@scenario('patch.feature', 'Patch a resource that exists')
def test_patch_a_resource_that_exists():
    """Patch a resource that exists."""
    pass


@when('I patch <group_version>.<kind> <name> in <namespace> with <update>')
def patch_resource_in_namespace(context, client, group_version, kind, name, namespace, update, definition_loader):
    """I patch <group_version>.<kind> <name> in <namespace> with <update>."""
    patch = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    context['instance'] = resource.patch(body=patch, namespace=namespace)


@when('I try to patch <group_version>.<kind> <name> in <namespace> with <update>')
def attempt_patch_resource_in_namespace(context, client, group_version, kind, name, namespace, update, definition_loader):
    """I try to patch <group_version>.<kind> <name> in <namespace> with <update>."""
    patch = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    try:
        context['instance'] = resource.patch(body=patch, namespace=namespace)
    except Exception as e:
        context['exc'] = e


@then('<group_version>.<kind> <name> in <namespace> should match the content of <update>')
def resource_should_match_update(context, client, group_version, kind, name, namespace, update, definition_loader, object_contains):
    """<group_version>.<kind> <name> in <namespace> should match the content of <update>."""
    patch = definition_loader(update)
    resource = client.resources.get(api_version=group_version, kind=kind)
    cluster_instance = resource.get(name=name, namespace=namespace).to_dict()
    assert object_contains(cluster_instance, patch)
