import io
import os
import tarfile
import time
import uuid

import docker
import pytest
import requests

from kubernetes import config
from openshift.helper import KubernetesObjectHelper

@pytest.fixture(scope='session')
def openshift_container(request):
    client = docker.from_env()
    # TODO: bind to a random host port
    image_name = 'openshift/origin:{}'.format(request.config.getoption('--openshift-version'))
    container = client.containers.run(image_name, 'start master', detach=True,
                                      ports={'8443/tcp': 8443})

    try:
        # Wait for the container to no longer be in the created state before
        # continuing
        while container.status == u'created':
            time.sleep(0.2)
            container = client.containers.get(container.id)

        # Wait for the api server to be ready before continuing
        # TODO: actually we end on a 200 response
        for _ in range(10):
            try:
                resp = requests.head("https://localhost:8443/healthz/ready", verify=False)
                if resp.status_code == 200:
                    break
            except requests.RequestException:
                pass

            time.sleep(1)

        # TODO: handle waiting for system policy to be fully configured better
        time.sleep(1)

        yield container
    finally:
        # Always remove the container
        container.remove(force=True)


@pytest.fixture(scope='session')
def kubeconfig(openshift_container, tmpdir_factory):
    # get_archive returns a stream of the tar archive containing the requested
    # files/directories, so we need use BytesIO as an intermediate step.
    tar_stream, _ = openshift_container.get_archive('/var/lib/origin/openshift.local.config/master/admin.kubeconfig')
    tar_obj = tarfile.open(fileobj=io.BytesIO(tar_stream.read()))
    kubeconfig_contents = tar_obj.extractfile('admin.kubeconfig').read()

    kubeconfig_file = tmpdir_factory.mktemp('kubeconfig').join('admin.kubeconfig')
    kubeconfig_file.write(kubeconfig_contents)
    yield kubeconfig_file


@pytest.fixture()
def k8s_helper_create(kubeconfig):
    def create_func(api_version, kind):
        k8s_helper = KubernetesObjectHelper(api_version, kind, debug=True)
        k8s_helper.set_client_config({'kubeconfig': str(kubeconfig)})
        config.kube_config.configuration.host='https://localhost:8443'
        return k8s_helper
    yield create_func


def pytest_generate_tests(metafunc):
    """
    Read .yml files from openshift/examples, parse the YAML, and pass it
    into the tests.
    :param metafunc: pytest metafunc obj
    :return: None
    """
    this_dir, _ = os.path.split(__file__)
    examples_path = os.path.normpath(os.path.join(this_dir, '../../examples'))
    if not os.path.exists(examples_path):
        raise Exception("ERROR: Unable to locate examples directory!!!")
    def get_ids(x):
        """
        Return an id for a given parameter dict.
        :param x: dict of test parameters
        :return: id string
        """
        return x['api_version'] + '_' + x['kind']
    parameters = []
    for example_file in os.listdir(examples_path):
        with open(os.path.join(examples_path, example_file), 'r') as f:
            api_version, kind = example_file.replace('.yml', '').split('_', 2)
            examples = ruamel.yaml.load(f.read(), ruamel.yaml.RoundTripLoader)
            param_dict = {
                'api_version': api_version,
                'kind': kind,
                'examples': examples
            }
            parameters.append(param_dict)
    metafunc.parametrize('params', parameters, ids=get_ids)
