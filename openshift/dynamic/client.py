#!/usr/bin/env python

import sys
import json
from functools import partial

import yaml
from pprint import pformat

from kubernetes import config
from kubernetes.client.api_client import ApiClient
from kubernetes.client.rest import ApiException

from openshift.dynamic.exceptions import ResourceNotFoundError, ResourceNotUniqueError, api_exception

__all__ = [
    'DynamicClient',
    'ResourceInstance',
    'Resource',
    'Subresource',
    'ResourceContainer',
    'ResourceField',
]


def meta_request(func):
    """ Handles parsing response structure and translating API Exceptions """
    def inner(self, resource, *args, **kwargs):
        serialize_response = kwargs.pop('serialize', True)
        try:
            resp = func(self, resource, *args, **kwargs)
        except ApiException as e:
            raise api_exception(e)
        if serialize_response:
            return serialize(resource, resp)
        return resp

    return inner

def serialize(resource, response):
    try:
        return ResourceInstance(resource, load_json(response))
    except ValueError:
        return response.data.decode()

def load_json(response):
    return json.loads(response.data.decode())


class DynamicClient(object):
    """ A kubernetes client that dynamically discovers and interacts with
        the kubernetes API
    """

    def __init__(self, client):
        self.client = client
        self.configuration = client.configuration
        self._load_server_info()
        self.__resources = ResourceContainer(self.parse_api_groups())

    def _load_server_info(self):
        self.__version = {'kubernetes': load_json(self.request('get', '/version'))}
        try:
            self.__version['openshift'] = load_json(self.request('get', '/version/openshift'))
        except ApiException:
            pass

    @property
    def resources(self):
        return self.__resources

    @property
    def version(self):
        return self.__version

    def default_groups(self):
        groups = {}
        groups['api'] = { '': {
            'v1': self.get_resources_for_api_version('api', '', 'v1', True)
        }}

        if self.version.get('openshift'):
            groups['oapi'] = { '': {
                'v1': self.get_resources_for_api_version('oapi', '', 'v1', True)
            }}

        return groups

    def parse_api_groups(self):
        """ Discovers all API groups present in the cluster """
        prefix = 'apis'
        groups_response = load_json(self.request('GET', '/{}'.format(prefix)))['groups']

        groups = self.default_groups()
        groups[prefix] = {}

        for group in groups_response:
            new_group = {}
            for version_raw in group['versions']:
                version = version_raw['version']
                preferred = version_raw == group['preferredVersion']
                new_group[version] = self.get_resources_for_api_version(prefix, group['name'], version, preferred)
            groups[prefix][group['name']] = new_group
        return groups

    def get_resources_for_api_version(self, prefix, group, version, preferred):
        """ returns a dictionary of resources associated with provided groupVersion"""

        resources = {}
        subresources = {}

        path = '/'.join(filter(None, [prefix, group, version]))
        resources_response = load_json(self.request('GET', path))['resources']

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

            resources[resource['kind']] = Resource(
                prefix=prefix,
                group=group,
                api_version=version,
                client=self,
                preferred=preferred,
                subresources=subresources.get(resource['name']),
                **resource
            )
        return resources

    def ensure_namespace(self, resource, namespace, body):
        namespace = namespace or body.get('metadata', {}).get('namespace')
        if not namespace:
            raise ValueError("Namespace is required for {}.{}".format(resource.group_version, resource.kind))
        return namespace

    def serialize_body(self, body):
        if isinstance(body, ResourceInstance):
            return body.to_dict()
        return body or {}

    @meta_request
    def get(self, resource, name=None, namespace=None, **kwargs):
        path = resource.path(name=name, namespace=namespace)
        return self.request('get', path, **kwargs)

    @meta_request
    def create(self, resource, body=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)
        path = resource.path(namespace=namespace)
        return self.request('post', path, body=body, **kwargs)

    @meta_request
    def delete(self, resource, name=None, namespace=None, label_selector=None, field_selector=None, **kwargs):
        if not (name or label_selector or field_selector):
            raise ValueError("At least one of name|label_selector|field_selector is required")
        if resource.namespaced and not (label_selector or field_selector or namespace):
            raise ValueError("At least one of namespace|label_selector|field_selector is required")
        path = resource.path(name=name, namespace=namespace)
        return self.request('delete', path, label_selector=label_selector, field_selector=field_selector, **kwargs)

    @meta_request
    def replace(self, resource, body=None, name=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        name = name or body.get('metadata', {}).get('name')
        if not name:
            raise ValueError("name is required to replace {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)
        path = resource.path(name=name, namespace=namespace)
        return self.request('put', path, body=body, **kwargs)

    @meta_request
    def patch(self, resource, body=None, name=None, namespace=None, **kwargs):
        body = self.serialize_body(body)
        name = name or body.get('metadata', {}).get('name')
        if not name:
            raise ValueError("name is required to patch {}.{}".format(resource.group_version, resource.kind))
        if resource.namespaced:
            namespace = self.ensure_namespace(resource, namespace, body)

        content_type = kwargs.pop('content_type', 'application/strategic-merge-patch+json')
        path = resource.path(name=name, namespace=namespace)

        return self.request('patch', path, body=body, content_type=content_type, **kwargs)


    def request(self, method, path, body=None, **params):

        if not path.startswith('/'):
            path = '/' + path

        path_params = params.get('path_params', {})
        query_params = params.get('query_params', [])
        if params.get('pretty'):
            query_params.append(('pretty', params['pretty']))
        if params.get('_continue'):
            query_params.append(('continue', params['_continue']))
        if params.get('include_uninitialized'):
            query_params.append(('includeUninitialized', params['include_uninitialized']))
        if params.get('field_selector'):
            query_params.append(('fieldSelector', params['field_selector']))
        if params.get('label_selector'):
            query_params.append(('labelSelector', params['label_selector']))
        if params.get('limit'):
            query_params.append(('limit', params['limit']))
        if params.get('resource_version'):
            query_params.append(('resourceVersion', params['resource_version']))
        if params.get('timeout_seconds'):
            query_params.append(('timeoutSeconds', params['timeout_seconds']))
        if params.get('watch'):
            query_params.append(('watch', params['watch']))

        header_params = params.get('header_params', {})
        form_params = []
        local_var_files = {}
        # HTTP header `Accept`
        header_params['Accept'] = self.client.select_header_accept([
            'application/json',
            'application/yaml',
            'application/vnd.kubernetes.protobuf'
        ])

        # HTTP header `Content-Type`
        if params.get('content_type'):
            header_params['Content-Type'] = params['content_type']
        else:
            header_params['Content-Type'] = self.client.select_header_content_type(['*/*'])

        # Authentication setting
        auth_settings = ['BearerToken']

        return self.client.call_api(
            path,
            method.upper(),
            path_params,
            query_params,
            header_params,
            body=body,
            post_params=form_params,
            async_req=params.get('async_req'),
            files=local_var_files,
            auth_settings=auth_settings,
            _preload_content=False,
            _return_http_data_only=params.get('_return_http_data_only', True)
        )


class Resource(object):
    """ Represents an API resource type, containing the information required to build urls for requests """

    def __init__(self, prefix=None, group=None, api_version=None, kind=None,
                 namespaced=False, verbs=None, name=None, preferred=False, client=None,
                 singularName=None, shortNames=None, categories=None, subresources=None, **kwargs):

        if None in (api_version, kind, prefix):
            raise ValueError("At least prefix, kind, and api_version must be provided")

        self.prefix = prefix
        self.group = group
        self.api_version = api_version
        self.kind = kind
        self.namespaced = namespaced
        self.verbs = verbs
        self.name = name
        self.preferred = preferred
        self.client = client
        self.singular_name = singularName or (name[:-1] if name else "")
        self.short_names = shortNames
        self.categories = categories
        self.subresources = {
            k: Subresource(self, **v) for k, v in (subresources or {}).items()
        }

        self.extra_args = kwargs

    @property
    def group_version(self):
        if self.group:
            return '{}/{}'.format(self.group, self.api_version)
        return self.api_version

    def __repr__(self):
        return '<{}({}/{}>)'.format(self.__class__.__name__, self.group_version, self.name)

    @property
    def urls(self):
        full_prefix = '{}/{}'.format(self.prefix, self.group_version)
        return {
            'base': '/{}/{}'.format(full_prefix, self.name),
            'namespaced_base': '/{}/namespaces/{{namespace}}/{}'.format(full_prefix, self.name),
            'full': '/{}/{}/{{name}}'.format(full_prefix, self.name),
            'namespaced_full': '/{}/namespaces/{{namespace}}/{}/{{name}}'.format(full_prefix, self.name)
        }

    def path(self, name=None, namespace=None):
        url_type = []
        path_params = {}
        if self.namespaced and namespace:
            url_type.append('namespaced')
            path_params['namespace'] = namespace
        if name:
            url_type.append('full')
            path_params['name'] = name
        else:
            url_type.append('base')
        return self.urls['_'.join(url_type)].format(**path_params)

    def __getattr__(self, name):
        if name in self.subresources:
            return self.subresources[name]
        return partial(getattr(self.client, name), self)


class Subresource(Resource):
    """ Represents a subresource of an API resource. This generally includes operations
        like scale, as well as status objects for an instantiated resource
    """

    def __init__(self, parent, **kwargs):
        self.parent = parent
        self.prefix = parent.prefix
        self.group = parent.group
        self.api_version = parent.api_version
        self.kind = kwargs.pop('kind')
        self.name = kwargs.pop('name')
        self.subresource = self.name.split('/')[1]
        self.namespaced = kwargs.pop('namespaced', False)
        self.verbs = kwargs.pop('verbs', None)
        self.extra_args = kwargs

    @property
    def urls(self):
        full_prefix = '{}/{}'.format(self.prefix, self.group_version)
        return {
            'full': '/{}/{}/{{name}}/{}'.format(full_prefix, self.parent.name, self.subresource),
            'namespaced_full': '/{}/namespaces/{{namespace}}/{}/{{name}}/{}'.format(full_prefix, self.parent.name, self.subresource)
        }

    def __getattr__(self, name):
        return partial(getattr(self.parent.client, name), self)


class ResourceContainer(object):
    """ A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources
    """

    def __init__(self, resources):
        self.__resources = resources

    @property
    def api_groups(self):
        """ list available api groups """
        return self.__resources['apis'].keys()

    def get(self, **kwargs):
        """ Same as search, but will throw an error if there are multiple or no
            results. If there are multiple results and only one is an exact match
            on api_version, that resource will be returned.
        """
        results = self.search(**kwargs)
        if len(results) > 1 and kwargs.get('api_version'):
            results = [
                result for result in results if result.group_version == kwargs['api_version']
            ]
        if len(results) == 1:
            return results[0]
        elif not results:
            raise ResourceNotFoundError('No matches found for {}'.format(kwargs))
        else:
            raise ResourceNotUniqueError('Multiple matches found for {}: {}'.format(kwargs, results))

    def search(self, **kwargs):
        """ Takes keyword arguments and returns matching resources. The search
            will happen in the following order:
                prefix: The api prefix for a resource, ie, /api, /oapi, /apis. Can usually be ignored
                group: The api group of a resource. Will also be extracted from api_version if it is present there
                api_version: The api version of a resource
                kind: The kind of the resource
                arbitrary arguments (see below), in random order

            The arbitrary arguments can be any valid attribute for an openshift.dynamic.Resource object
        """
        return self.__search(self.__build_search(**kwargs), self.__resources)

    def __build_search(self, kind=None, api_version=None, prefix=None, **kwargs):
        if api_version and '/' in api_version:
            group, version = api_version.split('/')
            items = [prefix, group, version, kind, kwargs]
        else:
            items = [prefix, '*', api_version, kind, kwargs]

        return list(map(lambda x: x or '*', items))

    def __search(self, parts, resources):
        part = parts[0]
        if part != '*' and resources.get(part):
            if isinstance(resources.get(part), dict):
                return self.__search(parts[1:], resources[part])
            else:
                resource = resources.get(part)
                if parts[1] != '*' and isinstance(parts[1], dict):
                    for term, value in parts[1].items():
                        if getattr(resource, term) == value:
                            return [resource]
                else:
                    return [resource]
        elif part == '*':
            matches = []
            for key in resources.keys():
                matches.extend(self.__search([key] + parts[1:], resources))
            return matches
        return []

    def __iter__(self):
        for _, groups in self.__resources.items():
            for _, versions in groups.items():
                for _, resources in versions.items():
                    for _, resource in resources.items():
                        yield resource


class ResourceField(object):
    """ A parsed instance of an API resource attribute. It exists
        solely to ease interaction with API objects by allowing
        attributes to be accessed with '.' notation
    """

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return pformat(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getitem__(self, name):
        return self.__dict__.get(name)

    # Here resource.items will return items if available or resource.__dict__.items function if not
    # resource.get will call resource.__dict__.get after attempting resource.__dict__.get('get')
    def __getattr__(self, name):
        return self.__dict__.get(name, getattr(self.__dict__, name, None))

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__.keys())

    def __iter__(self):
        for k, v in self.__dict__.items():
            yield (k, v)


class ResourceInstance(object):
    """ A parsed instance of an API resource. It exists solely to
        ease interaction with API objects by allowing attributes to
        be accessed with '.' notation.
    """

    def __init__(self, resource, instance):
        self.resource_type = resource
        self.attributes = self.__deserialize(instance)

    def __deserialize(self, field):
        if isinstance(field, dict):
            return ResourceField(**{
                k: self.__deserialize(v) for k, v in field.items()
            })
        elif isinstance(field, (list, tuple)):
            return [self.__deserialize(item) for item in field]
        else:
            return field

    def __serialize(self, field):
        if isinstance(field, ResourceField):
            return {
                k: self.__serialize(v) for k, v in field.__dict__.items()
            }
        elif isinstance(field, (list, tuple)):
            return [self.__serialize(item) for item in field]
        else:
            return field

    def to_dict(self):
        return self.__serialize(self.attributes)

    def to_str(self):
        return repr(self)

    def __repr__(self):
        return "ResourceInstance[{}]:\n  {}".format(
            self.attributes.kind,
            '  '.join(yaml.safe_dump(self.to_dict()).splitlines(True))
        )

    def __getattr__(self, name):
        return getattr(self.attributes, name)

    def __getitem__(self, name):
        return self.attributes[name]

    def __dir__(self):
        return dir(type(self)) + list(self.attributes.__dict__.keys())


def main():
    config.load_kube_config()
    client = DynamicClient(ApiClient())
    ret = {}
    for resource in client.resources:
        if resource.namespaced:
            key = resource.urls['namespaced_full']
        else:
            key = resource.urls['full']
        ret[key] = {k: v for k, v in resource.__dict__.items() if k not in ('client', 'subresources')}
        ret[key]['subresources'] = {}
        for name, value in resource.subresources.items():
            ret[key]['subresources'][name] = {k: v for k, v in value.__dict__.items() if k != 'parent'}

    print(yaml.safe_dump(ret))
    return 0


if __name__ == '__main__':
    sys.exit(main())
