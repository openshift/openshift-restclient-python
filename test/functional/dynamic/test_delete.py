# coding=utf-8
"""delete feature tests.
All step implementations are in conftest.py
"""

from pytest_bdd import scenario


@scenario('delete.feature', 'Delete a resource that exists')
def test_delete_a_resource_that_exists():
    """Delete a resource that exists"""
    pass


@scenario('delete.feature', 'Delete a resource that does not exist')
def test_delete_a_resource_that_does_not_exist():
    """Delete a resource that does not exist"""
    pass
