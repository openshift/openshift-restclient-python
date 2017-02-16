import copy
import pytest
import uuid

from openshift.helper import KubernetesObjectHelper

pytestmark = pytest.mark.functional

@pytest.fixture(scope='module')
def k8s_helper():
    k8s_helper = KubernetesObjectHelper('v1', 'project')
    return k8s_helper


@pytest.fixture()
def project(k8s_helper):
    name = "test-{}".format(uuid.uuid4())
    project_obj = k8s_helper.model(metadata={'name': name})
    project = k8s_helper.create_object(None, project_obj)
    assert project is not None
    assert project.kind == 'Project'
    assert project.api_version == 'v1'
    assert project.metadata.name == name

    yield project

    k8s_helper.delete_object(name)


@pytest.mark.skip()
def test_project_patch(k8s_helper, project):
    ns_copy = copy.deepcopy(project)
    ns_copy.metadata.labels = {'test-label': 'test-value'}
    patch_result = k8s_helper.patch_object(project.metadata.name, None, ns_copy)
    assert patch_result is not None
    assert patch_result.metadata.name == project.metadata.name
    assert patch_result != project
    assert patch_result.metadata.labels == {'test-label': 'test-value'}


def test_project_exists(k8s_helper, project):
    get_result = k8s_helper.get_object(project.metadata.name)
    assert get_result is not None
    assert get_result.metadata.name == project.metadata.name
    assert get_result == project


def test_get_exists_not(k8s_helper):
    name = "does-not-exist-{}".format(uuid.uuid4())
    project = k8s_helper.get_object(name)
    assert project is None
