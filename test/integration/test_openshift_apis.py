import unittest

import requests

from kubernetes import config
from kubernetes.client import api_client, Configuration

from openshift.dynamic import DynamicClient

class TestOpenshiftApis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            config.load_kube_config()
        except config.ConfigException:
            config.load_incluster_config()
        cls.config = Configuration.get_default_copy()

    def create_hello_openshift(self, client, namespace):
        apps_v1_deployments = client.resources.get(api_version='apps/v1', kind='Deployment')
        v1_services = client.resources.get(api_version='v1', kind='Service')

        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": "hello-openshift",
                "namespace": namespace
            },
            "spec": {
                "replicas": 3,
                "selector": {
                    "matchLabels": {
                        "app": "hello-openshift"
                    }
                },
                "template": {
                    "metadata": {
                        "labels": {
                            "app": "hello-openshift"
                        }
                    },
                    "spec": {
                        "containers": [{
                            "name": "hello-openshift",
                            "image": "docker.io/openshift/hello-openshift",
                            "ports": [{"containerPort": 8080}]
                        }]
                    }}}}
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": "hello-openshift",
                "namespace": namespace
            },
            "spec": {
                "ports": [{
                    "port": 80,
                    "targetPort": 8080
                }],
                "selector": {
                    "app": "hello-openshift"
                }
            }}
        apps_v1_deployments.create(deployment)
        v1_services.create(service)

    def test_v1_route(self):
        client = DynamicClient(api_client.ApiClient(configuration=self.config))
        v1_routes = client.resources.get(api_version='route.openshift.io/v1', kind='Route')
        self.create_hello_openshift(client, 'default')
        route = {
            "apiVersion": "route.openshift.io/v1",
            "kind": "Route",
            "metadata": {
                "name": "test-route",
                "namespace": "default",
            },
            "spec": {
                "to": {
                    "kind": "Service",
                    "name": "hello-openshift",
                },
                "port": {
                    "targetPort": 8080
                },
                "tls": {
                    "termination": "Edge",
                    "insecureEdgeTerminationPolicy": "Redirect",
                }
            }
        }
        created_route = v1_routes.create(route)
        url = created_route.spec.host
        response = requests.get("https://{0}".format(url), verify=False)
        assert "Hello Openshift!" in response.text

    def test_templates(self):
        client = DynamicClient(api_client.ApiClient(configuration=self.config))
        v1_templates = client.resources.get(api_version='template.openshift.io/v1', name='templates')
        v1_processed_templates = client.resources.get(api_version='template.openshift.io/v1', name='processedtemplates')

        nginx_template = v1_templates.get(name='nginx-example', namespace='openshift').to_dict()
        nginx_template = self.update_template_param(nginx_template, 'NAMESPACE', 'default')
        nginx_template = self.update_template_param(nginx_template, 'NAME', 'test123')

        response = v1_processed_templates.create(body=nginx_template, namespace='default')

        for obj in response.objects:
            if obj.metadata.namespace:
                assert obj.metadata.namespace == 'default'
            assert obj.metadata.name == 'test123'

    def update_template_param(self, template, k, v):
        for i, param in enumerate(template['parameters']):
            if param['name'] == k:
                template['parameters'][i]['value'] = v
                return template
        return template

