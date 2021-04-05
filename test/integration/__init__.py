import unittest

from kubernetes import config
from kubernetes.client import api_client, Configuration

from openshift.dynamic import DynamicClient

class RestClientTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        try:
            config.load_kube_config()
        except config.ConfigException:
            config.load_incluster_config()
        cls.config = Configuration.get_default_copy()
        cls.client = DynamicClient(api_client.ApiClient(configuration=cls.config))

    def setUp(self):
        # Generate a namespace name from the test case name
        self.namespace = self.id().split('.')[-1].replace('_', '-')
        v1_namespaces = self.client.resources.get(api_version='v1', kind='Namespace')

        self.addCleanup(v1_namespaces.delete, name=self.namespace)
        v1_namespaces.create(body=dict(
            apiVersion='v1',
            kind='Namespace',
            metadata=dict(name=self.namespace),
        ))
