import pytest

from kubernetes.client import ApiClient

from openshift.dynamic import DynamicClient, Resource, ResourceList


@pytest.fixture(scope='module')
def mock_namespace():
    return Resource(
        api_version='v1',
        kind='Namespace',
        name='namespaces',
        namespaced=False,
        preferred=True,
        prefix='api',
        shorter_names=['ns'],
        shortNames=['ns'],
        singularName='namespace',
        verbs=['create', 'delete', 'get', 'list', 'patch', 'update', 'watch']
    )


@pytest.fixture(scope='module')
def mock_namespace_list(mock_namespace):
    return ResourceList(mock_namespace)

@pytest.fixture(scope='function', autouse=True)
def setup_client_monkeypatch(monkeypatch, mock_namespace, mock_namespace_list):

    def mock_load_server_info(self):
        self.__version = {'kubernetes': 'mock-k8s-version'}

    def mock_parse_api_groups(self):
            return {
            'api': {
                '': {
                    'v1': {
                        'Namespace': mock_namespace,
                        'NamespaceList': mock_namespace_list
                    }
                }
            }
        }

    monkeypatch.setattr(DynamicClient, '_load_server_info', mock_load_server_info)
    monkeypatch.setattr(DynamicClient, 'parse_api_groups', mock_parse_api_groups)


@pytest.fixture()
def client():
    return DynamicClient(ApiClient())


@pytest.mark.parametrize(("attribute", "value"), [
    ('name', 'namespaces'),
    ('singular_name', 'namespace'),
    ('short_names', ['ns'])
])
def test_search_returns_single_and_list(client, mock_namespace, mock_namespace_list, attribute, value):
    resources = client.resources.search(**{'api_version':'v1', attribute: value})

    assert len(resources) == 2
    assert mock_namespace in resources
    assert mock_namespace_list in resources

@pytest.mark.parametrize(("attribute", "value"), [
    ('kind', 'Namespace'),
    ('name', 'namespaces'),
    ('singular_name', 'namespace'),
    ('short_names', ['ns'])
])
def test_get_returns_only_single(client, mock_namespace, attribute, value):
    resource = client.resources.get(**{'api_version':'v1', attribute: value})

    assert resource == mock_namespace


def test_get_namespace_list_kind(client, mock_namespace_list):
    resource = client.resources.get(api_version='v1', kind='NamespaceList')

    assert resource == mock_namespace_list
