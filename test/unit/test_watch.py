import json

from openshift import watch
from openshift import client
from openshift.client import models

from kubernetes import watch as k8s_watch
from kubernetes.client import models as k8s_models


def test_watch(monkeypatch):
    class MockHTTPResponse(object):

        def __init__(self, *args, **kwargs):
            pass

        def close(self):
            pass

        def release_conn(self):
            pass

    def mock_iter_resp_lines(resp):
        for name in ['test1', 'test2', 'test3']:
            yield json.dumps({
                'type': 'ADDED',
                'object': models.V1DeploymentConfig(
                    metadata=k8s_models.V1ObjectMeta(
                        name=name,
                        resource_version=1
                    )
                ).to_dict()
            })


    oapi = client.OapiApi()

    monkeypatch.setattr(oapi, 'list_deployment_config_for_all_namespaces', MockHTTPResponse)
    monkeypatch.setattr(k8s_watch.watch, 'iter_resp_lines', mock_iter_resp_lines)

    count = 2

    names = ['test1', 'test2', 'test3']
    w = watch.Watch(return_type="V1DeploymentConfig")
    for event in w.stream(oapi.list_deployment_config_for_all_namespaces, _request_timeout=2):
        assert event['object'].metadata.name in names
        names.remove(event['object'].metadata.name)
        count -= 1
        if not count:
            w.stop()
