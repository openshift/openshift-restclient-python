from kubernetes.dynamic.client import meta_request  # noqa
from kubernetes.dynamic.client import DynamicClient as K8sDynamicClient

from .apply import apply
from .discovery import EagerDiscoverer, LazyDiscoverer
from .resource import Resource, ResourceList, Subresource, ResourceInstance, ResourceField
from .exceptions import ApplyException

try:
    import kubernetes_validate  # noqa
    HAS_KUBERNETES_VALIDATE = True
except ImportError:
    HAS_KUBERNETES_VALIDATE = False

try:
    from kubernetes_validate.utils import VersionNotSupportedError
except ImportError:
    class VersionNotSupportedError(NotImplementedError):
        pass

__all__ = [
    'DynamicClient',
    'ResourceInstance',
    'Resource',
    'ResourceList',
    'Subresource',
    'EagerDiscoverer',
    'LazyDiscoverer',
    'ResourceField',
]


class DynamicClient(K8sDynamicClient):
    """ A kubernetes client that dynamically discovers and interacts with
        the kubernetes API
    """

    def __init__(self, client, cache_file=None, discoverer=None):
        discoverer = discoverer or LazyDiscoverer
        K8sDynamicClient.__init__(self, client, cache_file=cache_file, discoverer=discoverer)

    def apply(self, resource, body=None, name=None, namespace=None):
        body = self.serialize_body(body)
        body['metadata'] = body.get('metadata', dict())
        name = name or body['metadata'].get('name')
        if not name:
            raise ValueError("name is required to apply {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            body['metadata']['namespace'] = self.ensure_namespace(resource, namespace, body)
        try:
            return apply(resource, body)
        except ApplyException as e:
            raise ValueError("Could not apply strategic merge to %s/%s: %s" %
                             (body['kind'], body['metadata']['name'], e))
