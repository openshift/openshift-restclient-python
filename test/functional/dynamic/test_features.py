# coding=utf-8
"""Feature tests"""

from pytest_bdd import scenario


@scenario('create.feature', 'Create a resource again')
def test_create_a_resource_again():
    """Create a resource again."""
    pass


@scenario('create.feature', 'Create a resource for the first time')
def test_create_a_resource_for_the_first_time():
    """Create a resource for the first time."""
    pass


@scenario('delete.feature', 'Delete a resource that exists')
def test_delete_a_resource_that_exists():
    """Delete a resource that exists"""
    pass


@scenario('delete.feature', 'Delete a resource that does not exist')
def test_delete_a_resource_that_does_not_exist():
    """Delete a resource that does not exist"""
    pass
