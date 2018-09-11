import pytest
from pytest_bdd import scenario, then, parsers

from openshift.dynamic import exceptions


@scenario('delete.feature', 'Delete a resource that exists')
def test_delete_a_resource_that_exists():
    """Delete a resource that exists"""
    pass


@scenario('delete.feature', 'Delete a resource that does not exist')
def test_delete_a_resource_that_does_not_exist():
    """Delete a resource that does not exist"""
    pass


@then(parsers.parse('<group_version>.<kind> <name> does not exist in <namespace>'))
def resource_not_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> does not exist in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    with pytest.raises(exceptions.NotFoundError):
        resource.get(name, namespace)
