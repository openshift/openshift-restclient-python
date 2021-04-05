import time
import unittest
from datetime import datetime

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

    def create_namespace(self, client, namespace):
        v1_namespaces = client.resources.get(api_version='v1', kind='Namespace')
        self.addCleanup(v1_namespaces.delete, name=namespace)
        v1_namespaces.create(body=dict(
            apiVersion='v1',
            kind='Namespace',
            metadata=dict(name=namespace),
        ))

    def create_hello_openshift(self, client, namespace):
        apps_v1_deployments = client.resources.get(api_version='apps/v1', kind='Deployment')
        v1_services = client.resources.get(api_version='v1', kind='Service')

        name = 'hello-openshift'

        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": name,
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
                "name": name,
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
        self.addCleanup(apps_v1_deployments.delete, name=name, namespace=namespace)
        apps_v1_deployments.create(deployment)

        self.addCleanup(v1_services.delete, name=name, namespace=namespace)
        v1_services.create(service)

        # Wait 1 minute for deployment to become available
        timeout = 60
        start = datetime.now()
        while (datetime.now() - start).seconds < timeout:
            try:
                deployment = apps_v1_deployments.get(name=name, namespace=namespace)
                if (deployment.status
                    and deployment.spec.replicas == (deployment.status.replicas or 0)
                    and deployment.status.readyReplicas == deployment.spec.replicas
                    and deployment.status.observedGeneration == deployment.metadata.generation
                    and not deployment.status.unavailableReplicas):
                    return
                time.sleep(1)
            except Exception:
                time.sleep(1)

    def test_v1_route(self):
        namespace = 'osrcp-test-route'
        client = DynamicClient(api_client.ApiClient(configuration=self.config))
        self.create_namespace(client, namespace)
        v1_routes = client.resources.get(api_version='route.openshift.io/v1', kind='Route')
        self.create_hello_openshift(client, namespace)
        route = {
            "apiVersion": "route.openshift.io/v1",
            "kind": "Route",
            "metadata": {
                "name": "test-route",
                "namespace": namespace,
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
        self.addCleanup(v1_routes.delete, name='test-route', namespace=namespace)
        created_route = v1_routes.create(route)
        url = created_route.spec.host
        timeout = 10
        start = datetime.now()
        while (datetime.now() - start).seconds < timeout:
            response = requests.get("https://{0}".format(url), verify=False)
            if response.status_code == 200:
                break
        assert response.text == "Hello OpenShift!\n"

    def test_templates(self):
        namespace = 'osrcp-test-templates'
        client = DynamicClient(api_client.ApiClient(configuration=self.config))
        self.create_namespace(client, namespace)
        v1_templates = client.resources.get(api_version='template.openshift.io/v1', name='templates')
        v1_processed_templates = client.resources.get(api_version='template.openshift.io/v1', name='processedtemplates')

        nginx_template = v1_templates.get(name='nginx-example', namespace='openshift').to_dict()
        nginx_template = self.update_template_param(nginx_template, 'NAMESPACE', namespace)
        nginx_template = self.update_template_param(nginx_template, 'NAME', 'test123')

        response = v1_processed_templates.create(body=nginx_template, namespace=namespace)

        for obj in response.objects:
            if obj.metadata.namespace:
                assert obj.metadata.namespace == namespace
            assert obj.metadata.name == 'test123'

    def update_template_param(self, template, k, v):
        for i, param in enumerate(template['parameters']):
            if param['name'] == k:
                template['parameters'][i]['value'] = v
                return template
        return template
