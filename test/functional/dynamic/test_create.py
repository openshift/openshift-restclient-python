# coding=utf-8
"""create feature tests.
All step implementations are in conftest.py
"""

from pytest_bdd import scenario


@scenario('create.feature', 'Create a resource again')
def test_create_a_resource_again():
    """Create a resource again."""
    pass


@scenario('create.feature', 'Create a resource for the first time')
def test_create_a_resource_for_the_first_time():
    """Create a resource for the first time."""
    pass
