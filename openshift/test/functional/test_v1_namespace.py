import copy
import pytest
import uuid

from openshift.helper import KubernetesObjectHelper


@pytest.fixture()
def namespace(k8s_helper):
    name = "test-{}".format(uuid.uuid4())
    namespace_obj = k8s_helper.model(metadata={'name': name})
    namespace = k8s_helper.create_object(None, namespace_obj)
    assert namespace is not None
    assert namespace.kind == 'Namespace'
    assert namespace.api_version == 'v1'
    assert namespace.metadata.name == name

    yield namespace

    k8s_helper.delete_object(name, None)


def test_namespace_patch(k8s_helper, namespace):
    ns_copy = copy.deepcopy(namespace)
    ns_copy.metadata.labels = {'test-label': 'test-value'}
    patch_result = k8s_helper.patch_object(namespace.metadata.name, None, ns_copy)
    assert patch_result is not None
    assert patch_result.metadata.name == namespace.metadata.name
    assert patch_result != namespace
    assert patch_result.metadata.labels == {'test-label': 'test-value'}


def test_namespace_exists(k8s_helper, namespace):
    get_result = k8s_helper.get_object(namespace.metadata.name)
    assert get_result is not None
    assert get_result.metadata.name == namespace.metadata.name
    assert get_result.metadata.uid == namespace.metadata.uid


def test_get_exists_not(k8s_helper):
    name = "does-not-exist-{}".format(uuid.uuid4())
    result = k8s_helper.get_object(name)
    assert result is None
