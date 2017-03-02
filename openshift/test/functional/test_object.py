import copy
import pytest
import uuid


@pytest.fixture()
def k8s_object(k8s_helper_create, params):
    k8sobj = None
    k8s_helper = k8s_helper_create(params['api_version'], params['kind'])
    project = None
    project_helper = None
    examples = params['examples']['examples']
    for example in examples:
        if example.get('create'):
            if example['create'].get('namespace') or example['create'].get('project'):
                name = example['create'].get('namespace', example['create'].get('project'))
                project_helper = k8s_helper_create(params['api_version'], 'project')
                project = project_helper.object_from_params({'name': name})
                project_helper.create_object(None, project)
            k8sobj = k8s_helper.object_from_params(example['create'])
            k8sobj = k8s_helper.create_object(k8sobj.metadata.namespace, k8sobj)
            for assertion in example['assertions']:
                assert(eval(assertion))
            break

    yield k8sobj

    # Remove objects after each test completes
    k8s_helper.delete_object(k8sobj.metadata.name, k8sobj.metadata.namespace, wait=True)
    if project_helper:
        project_helper.delete_object(project.metadata.name, None, wait=True)


def test_object_patch(k8s_helper_create, k8s_object, params):
    if params['kind'] == 'project':
        pytest.skip("Project fields are immutable")
    k8s_helper = k8s_helper_create(params['api_version'], params['kind'])
    examples = params['examples']['examples']
    for example in examples:
        if example.get('patch'):
            k8sobj = copy.deepcopy(k8s_object)
            k8s_helper.object_compare(k8sobj, example['patch'])
            k8sobj = k8s_helper.patch_object(k8s_object.metadata.name, k8s_object.metadata.namespace, k8sobj)
            assert k8sobj is not None
            for assertion in example['assertions']:
                assert(eval(assertion))


def test_object_exists(k8s_helper_create, k8s_object, params):
    k8s_helper = k8s_helper_create(params['api_version'], params['kind'])
    k8sobj = k8s_helper.get_object(k8s_object.metadata.name, k8s_object.metadata.namespace)
    assert k8sobj is not None


def test_get_exists_not(k8s_helper_create, params):
    examples = params['examples']['examples']
    namespace = None
    for example in examples:
        if example.get('create'):
            namespace = example['create'].get('namespace')
            break;
    k8s_helper = k8s_helper_create(params['api_version'], params['kind'])
    name = "does-not-exist-{}".format(uuid.uuid4())
    k8sobj = k8s_helper.get_object(name, namespace=namespace)
    assert k8sobj is None
