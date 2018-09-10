import re
import uuid

import pytest

from pkg_resources import parse_version

from kubernetes.client import V1Namespace, V1ObjectMeta
from openshift.helper.ansible import KubernetesAnsibleModuleHelper, OpenShiftAnsibleModuleHelper
def parse_test_name(name):
    pieces = re.findall('[A-Z][a-z0-9]*', name)
    cluster_type = pieces[1].lower()
    api_version = pieces[2].lower()
    resource = '_'.join(map(str.lower, pieces[3:]))
    return cluster_type, api_version, resource


@pytest.fixture(scope='class')
def ansible_helper(request, auth):
    cluster_type, api_version, resource = parse_test_name(request.node.name)
    if cluster_type == 'k8s':
        helper = KubernetesAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)
    else:
        helper = OpenShiftAnsibleModuleHelper(api_version, resource, debug=True, reset_logfile=False, **auth)

    helper.api_client.configuration.debug = True

    return helper


@pytest.fixture()
def object_name(request):
    action = request.function.__name__.split('_')[1]
    return '{}-{}'.format(action, uuid.uuid4())[:22].strip('-')


@pytest.fixture(scope='class')
def namespace(auth):
    name = "test-{}".format(uuid.uuid4())

    helper = KubernetesAnsibleModuleHelper('v1', 'namespace', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_object(V1Namespace(metadata=V1ObjectMeta(name=name)))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


@pytest.fixture(scope='class')
def project(auth):
    name = "test-{}".format(uuid.uuid4())
    helper = OpenShiftAnsibleModuleHelper('v1', 'project', debug=True, reset_logfile=False, **auth)

    k8s_obj = helper.create_project(metadata=V1ObjectMeta(name=name))
    assert k8s_obj is not None

    yield name

    helper.delete_object(name, None)


@pytest.fixture(autouse=True)
def skip_empty(request):
    _, api_version, resource = parse_test_name(request.node.cls._type)
    action = request.function.__name__.split('_')[1]
    tasks = list(filter(lambda x: x.get(action), request.node.cls.tasks['tasks']))
    if not tasks and action not in ['get', 'remove']:
        pytest.skip('No example provided to {} {}'.format(action, resource))


@pytest.fixture(autouse=True)
def skip_by_version(request, openshift_version):
    if request.node.cls.tasks.get('version_limits') and openshift_version:
        lowest_version = request.node.cls.tasks['version_limits'].get('min')
        highest_version = request.node.cls.tasks['version_limits'].get('max')
        skip_latest = request.node.cls.tasks['version_limits'].get('skip_latest')

        too_low = lowest_version and parse_version(lowest_version) > parse_version(openshift_version)
        too_high = highest_version and parse_version(highest_version) < parse_version(openshift_version)

        if openshift_version == 'latest':
            if skip_latest:
                pytest.skip('This API is not supported in the latest openshift version')
        elif too_low:
            pytest.skip('This API is not supported in openshift versions > {}. You are using version {}'.format(lowest_version, openshift_version))
        elif too_high:
            pytest.skip('This API is not supported in openshift versions < {}. You are using version {}'.format(highest_version, openshift_version))


def _get_id(argvalue):
    op_type = ''
    if argvalue.get('create'):
        op_type = 'create'
    elif argvalue.get('patch'):
        op_type = 'patch'
    elif argvalue.get('remove'):
        op_type = 'remove'
    elif argvalue.get('replace'):
        op_type = 'replace'
    return op_type + '_' + argvalue[op_type]['name'] + '_' + "{:0>3}".format(argvalue['seq'])
