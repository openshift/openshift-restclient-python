import time
from datetime import datetime

import requests

from . import RestClientTestCase

class TestOpenshiftApis(RestClientTestCase):

    def create_hello_openshift(self):
        apps_v1_deployments = self.client.resources.get(api_version='apps/v1', kind='Deployment')
        v1_services = self.client.resources.get(api_version='v1', kind='Service')

        name = 'hello-openshift'

        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": name,
                "namespace": self.namespace
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
                "namespace": self.namespace
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
        self.addCleanup(apps_v1_deployments.delete, name=name, namespace=self.namespace)
        apps_v1_deployments.create(deployment)

        self.addCleanup(v1_services.delete, name=name, namespace=self.namespace)
        v1_services.create(service)

        # Wait 1 minute for deployment to become available
        timeout = 60
        start = datetime.now()
        while (datetime.now() - start).seconds < timeout:
            try:
                deployment = apps_v1_deployments.get(name=name, namespace=self.namespace)
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
        self.create_hello_openshift()

        v1_routes = self.client.resources.get(api_version='route.openshift.io/v1', kind='Route')
        route = {
            "apiVersion": "route.openshift.io/v1",
            "kind": "Route",
            "metadata": {
                "name": "test-route",
                "namespace": self.namespace,
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

        self.addCleanup(v1_routes.delete, name='test-route', namespace=self.namespace)
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
        v1_templates = self.client.resources.get(api_version='template.openshift.io/v1', name='templates')
        v1_processed_templates = self.client.resources.get(api_version='template.openshift.io/v1', name='processedtemplates')

        nginx_template = v1_templates.get(name='nginx-example', namespace='openshift').to_dict()
        nginx_template = self.update_template_param(nginx_template, 'NAMESPACE', self.namespace)
        nginx_template = self.update_template_param(nginx_template, 'NAME', 'test123')

        response = v1_processed_templates.create(body=nginx_template, namespace=self.namespace)

        for obj in response.objects:
            if obj.metadata.namespace:
                assert obj.metadata.namespace == self.namespace
            assert obj.metadata.name == 'test123'

    def update_template_param(self, template, k, v):
        for i, param in enumerate(template['parameters']):
            if param['name'] == k:
                template['parameters'][i]['value'] = v
                return template
        return template
