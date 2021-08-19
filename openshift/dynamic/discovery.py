import os
import six
import hashlib
import tempfile
from collections import defaultdict

from urllib3.exceptions import ProtocolError, MaxRetryError

from kubernetes.dynamic.discovery import Discoverer as K8sDiscoverer
from kubernetes.dynamic.discovery import LazyDiscoverer as K8sLazyDiscoverer
from kubernetes.dynamic.discovery import LazyDiscoverer as K8sEagerDiscoverer
from kubernetes.dynamic.discovery import (  # noqa
    CacheEncoder,
    CacheDecoder,
    DISCOVERY_PREFIX,
    ResourceGroup,
)
from kubernetes.dynamic.exceptions import (
    ApiException,
    ResourceNotFoundError,
    ResourceNotUniqueError,
    ServiceUnavailableError,
)

from .resource import Resource, ResourceList


class Discoverer(K8sDiscoverer):
    """
        A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        Subclasses implement the abstract methods with different loading strategies.
    """

    def __init__(self, client, cache_file):
        self.client = client
        default_cachefile_name = 'osrcp-{0}.json'.format(hashlib.sha1(self.__get_default_cache_id()).hexdigest())
        self.__cache_file = cache_file or os.path.join(tempfile.gettempdir(), default_cachefile_name)
        self.__init_cache()

    def __get_default_cache_id(self):
        user = self.__get_user()
        if user:
            cache_id = "{0}-{1}".format(self.client.configuration.host, user)
        else:
            cache_id = self.client.configuration.host

        if six.PY3:
            return cache_id.encode('utf-8')

        return cache_id

    def __get_user(self):
        if hasattr(os, 'getlogin'):
            try:
                user = os.getlogin()
                if user:
                    return str(user)
            except OSError:
                pass
        if hasattr(os, 'getuid'):
            try:
                user = os.getuid()
                if user:
                    return str(user)
            except OSError:
                pass
        user = os.environ.get("USERNAME")
        if user:
            return str(user)
        return None

    def default_groups(self, request_resources=False):
        groups = {}
        groups['api'] = { '': {
            'v1': (ResourceGroup( True, resources=self.get_resources_for_api_version('api', '', 'v1', True) )
                if request_resources else ResourceGroup(True))
        }}

        if self.version.get('openshift'):
            groups['oapi'] = { '': {
                'v1': (ResourceGroup( True, resources=self.get_resources_for_api_version('oapi', '', 'v1', True) )
                    if request_resources else ResourceGroup(True))
                }}
        groups[DISCOVERY_PREFIX] = {'': {
            'v1': ResourceGroup(True, resources = {"List": [ResourceList(self.client)]})
        }}
        return groups

    def _load_server_info(self):
        def just_json(_, serialized):
            return serialized

        if not self._cache.get('version'):
            try:
                self._cache['version'] = {
                    'kubernetes': self.client.request('get', '/version', serializer=just_json)
                }
            except (ValueError, MaxRetryError) as e:
                if isinstance(e, MaxRetryError) and not isinstance(e.reason, ProtocolError):
                    raise
                if not self.client.configuration.host.startswith("https://"):
                    raise ValueError("Host value %s should start with https:// when talking to HTTPS endpoint" %
                                     self.client.configuration.host)
                else:
                    raise
            try:
                self._cache['version']['openshift'] = self.client.request(
                    'get',
                    '/version/openshift',
                    serializer=just_json,
                )
            except ApiException:
                pass
        self.__version = self._cache['version']

    def get_resources_for_api_version(self, prefix, group, version, preferred):
        """ returns a dictionary of resources associated with provided (prefix, group, version)"""

        resources = defaultdict(list)
        subresources = {}

        path = '/'.join(filter(None, [prefix, group, version]))
        try:
            resources_response = self.client.request('GET', path).resources or []
        except ServiceUnavailableError:
            resources_response = []

        resources_raw = list(filter(lambda resource: '/' not in resource['name'], resources_response))
        subresources_raw = list(filter(lambda resource: '/' in resource['name'], resources_response))
        for subresource in subresources_raw:
            resource, name = subresource['name'].split('/')
            if not subresources.get(resource):
                subresources[resource] = {}
            subresources[resource][name] = subresource

        for resource in resources_raw:
            # Prevent duplicate keys
            for key in ('prefix', 'group', 'api_version', 'client', 'preferred'):
                resource.pop(key, None)

            resourceobj = Resource(
                prefix=prefix,
                group=group,
                api_version=version,
                client=self.client,
                preferred=preferred,
                subresources=subresources.get(resource['name']),
                **resource
            )
            resources[resource['kind']].append(resourceobj)

            resource_lookup = {
                'prefix': prefix,
                'group': group,
                'api_version': version,
                'kind': resourceobj.kind,
                'name': resourceobj.name
            }
            resource_list = ResourceList(self.client, group=group, api_version=version, base_kind=resource['kind'], base_resource_lookup=resource_lookup)
            resources[resource_list.kind].append(resource_list)
        return resources

    def get(self, **kwargs):
        """ Same as search, but will throw an error if there are multiple or no
            results. If there are multiple results and only one is an exact match
            on api_version, that resource will be returned.
        """
        results = self.search(**kwargs)
        # If there are multiple matches, prefer exact matches on api_version
        if len(results) > 1 and kwargs.get('api_version'):
            results = [
                result for result in results if result.group_version == kwargs['api_version']
            ]
        # If there are multiple matches, prefer non-List kinds
        if len(results) > 1 and not all([isinstance(x, ResourceList) for x in results]):
            results = [result for result in results if not isinstance(result, ResourceList)]
        # if multiple resources are found that share a GVK, prefer the one with the most supported verbs
        if len(results) > 1 and len(set((x.group_version, x.kind) for x in results)) == 1:
            if len(set(len(x.verbs) for x in results)) != 1:
                results = [max(results, key=lambda x: len(x.verbs))]
        if len(results) == 1:
            return results[0]
        elif not results:
            raise ResourceNotFoundError('No matches found for {}'.format(kwargs))
        else:
            raise ResourceNotUniqueError('Multiple matches found for {}: {}'.format(kwargs, results))


class LazyDiscoverer(K8sLazyDiscoverer, Discoverer):
    """ A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        Resources for the cluster are loaded lazily.
    """


class EagerDiscoverer(K8sEagerDiscoverer, Discoverer):
    """ A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        All resources are discovered for the cluster upon object instantiation.
    """
