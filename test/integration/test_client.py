import time
import uuid

from openshift.dynamic.exceptions import ResourceNotFoundError

from . import RestClientTestCase


def short_uuid():
    id = str(uuid.uuid4())
    return id[-12:]


class TestDynamicClient(RestClientTestCase):

    def test_cluster_custom_resources(self):
        with self.assertRaises(ResourceNotFoundError):
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ClusterChangeMe')

        crd_api = self.client.resources.get(
            api_version='apiextensions.k8s.io/v1beta1',
            kind='CustomResourceDefinition')
        name = 'clusterchangemes.apps.example.com'
        crd_manifest = {
            'apiVersion': 'apiextensions.k8s.io/v1beta1',
            'kind': 'CustomResourceDefinition',
            'metadata': {
                'name': name,
            },
            'spec': {
                'group': 'apps.example.com',
                'names': {
                    'kind': 'ClusterChangeMe',
                    'listKind': 'ClusterChangeMeList',
                    'plural': 'clusterchangemes',
                    'singular': 'clusterchangeme',
                },
                'scope': 'Cluster',
                'version': 'v1',
                'subresources': {
                    'status': {}
                }
            }
        }
        resp = crd_api.create(crd_manifest)

        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = crd_api.get(
            name=name,
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        try:
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ClusterChangeMe')
        except ResourceNotFoundError:
            # Need to wait a sec for the discovery layer to get updated
            time.sleep(2)
        changeme_api = self.client.resources.get(
            api_version='apps.example.com/v1', kind='ClusterChangeMe')
        resp = changeme_api.get()
        self.assertEqual(resp.items, [])
        changeme_name = 'custom-resource' + short_uuid()
        changeme_manifest = {
            'apiVersion': 'apps.example.com/v1',
            'kind': 'ClusterChangeMe',
            'metadata': {
                'name': changeme_name,
            },
            'spec': {}
        }

        resp = changeme_api.create(body=changeme_manifest)
        self.assertEqual(resp.metadata.name, changeme_name)

        resp = changeme_api.get(name=changeme_name)
        self.assertEqual(resp.metadata.name, changeme_name)

        changeme_manifest['spec']['size'] = 3
        resp = changeme_api.patch(
            body=changeme_manifest,
            content_type='application/merge-patch+json'
        )
        self.assertEqual(resp.spec.size, 3)

        resp = changeme_api.get(name=changeme_name)
        self.assertEqual(resp.spec.size, 3)

        resp = changeme_api.get()
        self.assertEqual(len(resp.items), 1)

        resp = changeme_api.delete(
            name=changeme_name,
        )

        resp = changeme_api.get()
        self.assertEqual(len(resp.items), 0)

        resp = crd_api.delete(
            name=name,
        )

        time.sleep(2)
        self.client.resources.invalidate_cache()
        with self.assertRaises(ResourceNotFoundError):
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ClusterChangeMe')

    def test_namespaced_custom_resources(self):
        with self.assertRaises(ResourceNotFoundError):
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ChangeMe')

        crd_api = self.client.resources.get(
            api_version='apiextensions.k8s.io/v1beta1',
            kind='CustomResourceDefinition')
        name = 'changemes.apps.example.com'
        crd_manifest = {
            'apiVersion': 'apiextensions.k8s.io/v1beta1',
            'kind': 'CustomResourceDefinition',
            'metadata': {
                'name': name,
            },
            'spec': {
                'group': 'apps.example.com',
                'names': {
                    'kind': 'ChangeMe',
                    'listKind': 'ChangeMeList',
                    'plural': 'changemes',
                    'singular': 'changeme',
                },
                'scope': 'Namespaced',
                'version': 'v1',
                'subresources': {
                    'status': {}
                }
            }
        }
        resp = crd_api.create(crd_manifest)

        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = crd_api.get(
            name=name,
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        try:
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ChangeMe')
        except ResourceNotFoundError:
            # Need to wait a sec for the discovery layer to get updated
            time.sleep(2)
        changeme_api = self.client.resources.get(
            api_version='apps.example.com/v1', kind='ChangeMe')
        resp = changeme_api.get()
        self.assertEqual(resp.items, [])
        changeme_name = 'custom-resource' + short_uuid()
        changeme_manifest = {
            'apiVersion': 'apps.example.com/v1',
            'kind': 'ChangeMe',
            'metadata': {
                'name': changeme_name,
            },
            'spec': {}
        }

        resp = changeme_api.create(body=changeme_manifest, namespace=self.namespace)
        self.assertEqual(resp.metadata.name, changeme_name)

        resp = changeme_api.get(name=changeme_name, namespace=self.namespace)
        self.assertEqual(resp.metadata.name, changeme_name)

        changeme_manifest['spec']['size'] = 3
        resp = changeme_api.patch(
            body=changeme_manifest,
            namespace=self.namespace,
            content_type='application/merge-patch+json'
        )
        self.assertEqual(resp.spec.size, 3)

        resp = changeme_api.get(name=changeme_name, namespace=self.namespace)
        self.assertEqual(resp.spec.size, 3)

        resp = changeme_api.get(namespace=self.namespace)
        self.assertEqual(len(resp.items), 1)

        resp = changeme_api.get()
        self.assertEqual(len(resp.items), 1)

        resp = changeme_api.delete(
            name=changeme_name,
            namespace=self.namespace
        )

        resp = changeme_api.get(namespace=self.namespace)
        self.assertEqual(len(resp.items), 0)

        resp = changeme_api.get()
        self.assertEqual(len(resp.items), 0)

        resp = crd_api.delete(
            name=name,
        )

        time.sleep(2)
        self.client.resources.invalidate_cache()
        with self.assertRaises(ResourceNotFoundError):
            changeme_api = self.client.resources.get(
                api_version='apps.example.com/v1', kind='ChangeMe')

    def test_service_apis(self):
        api = self.client.resources.get(api_version='v1', kind='Service')

        name = 'frontend-' + short_uuid()
        service_manifest = {'apiVersion': 'v1',
                            'kind': 'Service',
                            'metadata': {'labels': {'name': name},
                                         'name': name,
                                         'resourceversion': 'v1'},
                            'spec': {'ports': [{'name': 'port',
                                                'port': 80,
                                                'protocol': 'TCP',
                                                'targetPort': 80}],
                                     'selector': {'name': name}}}

        resp = api.create(
            body=service_manifest,
            namespace=self.namespace
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        resp = api.get(
            name=name,
            namespace=self.namespace
        )
        self.assertEqual(name, resp.metadata.name)
        self.assertTrue(resp.status)

        service_manifest['spec']['ports'] = [{'name': 'new',
                                              'port': 8080,
                                              'protocol': 'TCP',
                                              'targetPort': 8080}]
        resp = api.patch(
            body=service_manifest,
            name=name,
            namespace=self.namespace
        )
        self.assertEqual(2, len(resp.spec.ports))
        self.assertTrue(resp.status)

        resp = api.delete(
            name=name, body={},
            namespace=self.namespace
        )

    def test_replication_controller_apis(self):
        api = self.client.resources.get(
            api_version='v1', kind='ReplicationController')

        name = 'frontend-' + short_uuid()
        rc_manifest = {
            'apiVersion': 'v1',
            'kind': 'ReplicationController',
            'metadata': {'labels': {'name': name},
                         'name': name},
            'spec': {'replicas': 2,
                     'selector': {'name': name},
                     'template': {'metadata': {
                         'labels': {'name': name}},
                         'spec': {'containers': [{
                             'image': 'nginx',
                             'name': 'nginx',
                             'ports': [{'containerPort': 80,
                                        'protocol': 'TCP'}]}]}}}}

        resp = api.create(
            body=rc_manifest, namespace=self.namespace)
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.get(
            name=name, namespace=self.namespace)
        self.assertEqual(name, resp.metadata.name)
        self.assertEqual(2, resp.spec.replicas)

        resp = api.delete(
            name=name, body={}, namespace=self.namespace)

    def test_configmap_apis(self):
        api = self.client.resources.get(api_version='v1', kind='ConfigMap')

        name = 'test-configmap-' + short_uuid()
        test_configmap = {
            "kind": "ConfigMap",
            "apiVersion": "v1",
            "metadata": {
                "name": name,
            },
            "data": {
                "config.json": "{\"command\":\"/usr/bin/mysqld_safe\"}",
                "frontend.cnf": "[mysqld]\nbind-address = 10.0.0.3\n"
            }
        }

        resp = api.create(
            body=test_configmap, namespace=self.namespace
        )
        self.assertEqual(name, resp.metadata.name)

        resp = api.get(
            name=name, namespace=self.namespace)
        self.assertEqual(name, resp.metadata.name)

        test_configmap['data']['config.json'] = "{}"
        resp = api.patch(
            name=name, namespace=self.namespace, body=test_configmap)

        resp = api.delete(
            name=name, body={}, namespace=self.namespace)

        resp = api.get(namespace=self.namespace, pretty=True)
        self.assertEqual([], resp.items)

    def test_node_apis(self):
        api = self.client.resources.get(api_version='v1', kind='Node')

        for item in api.get().items:
            node = api.get(name=item.metadata.name)
            self.assertTrue(len(dict(node.metadata.labels)) > 0)
