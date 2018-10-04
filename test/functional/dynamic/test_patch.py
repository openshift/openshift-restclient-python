# coding=utf-8
"""Patch feature tests.
All step implementations are in conftest.py
"""

from pytest_bdd import scenario


@scenario('patch.feature', 'Patch a resource that does not exist')
def test_patch_a_resource_that_does_not_exist():
    """Patch a resource that does not exist."""
    pass


@scenario('patch.feature', 'Patch a resource that exists')
def test_patch_a_resource_that_exists():
    """Patch a resource that exists."""
    pass
