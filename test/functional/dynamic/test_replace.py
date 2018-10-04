# coding=utf-8
"""replace feature tests.
All step implementations are in conftest.py
"""

from pytest_bdd import scenario


@scenario('replace.feature', 'Replace a resource that does not exist')
def test_replace_a_resource_that_does_not_exist():
    """replace a resource that does not exist."""
    pass


@scenario('replace.feature', 'Replace a resource that exists')
def test_replace_a_resource_that_exists():
    """replace a resource that exists."""
    pass
