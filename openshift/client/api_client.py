from kubernetes.client.api_client import ApiClient as K8sApiClient

class ApiClient(K8sApiClient):
    def _ApiClient__deserialize(self, data, klass):
        try:
            return super(ApiClient, self).__deserialize(data, klass)
        except AttributeError:
            klass = eval('models.' + klass)
            return super(ApiClient, self).__deserialize_model(data, klass)
