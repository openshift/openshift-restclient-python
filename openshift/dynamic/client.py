#!/usr/bin/env python

import sys
import json
from functools import partial

import yaml
from pprint import pformat

from kubernetes import config
from kubernetes.client.api_client import ApiClient
from kubernetes.client.rest import ApiException


class DynamicClient(object):

    def __init__(self, client):
        self.client = client
        self.__resources = ResourceContainer(self.parse_api_groups())

    @property
    def resources(self):
        return self.__resources

    def default_groups(self):
        groups = {}
        groups['api'] = { '': {
            'v1': self.get_resources_for_apiversion('api', '', 'v1', True)
        }}

        try:
            self.request('get', '/version/openshift')
            is_openshift = True
        except ApiException:
            is_openshift = False

        if is_openshift:
            groups['oapi'] = { '': {
                'v1': self.get_resources_for_apiversion('oapi', '', 'v1', True)
            }}
        return groups

    def parse_api_groups(self):
        ""
        prefix = 'apis'
        groups_response = self.request('GET', '/{}'.format(prefix))['groups']

        groups = self.default_groups()
        groups[prefix] = {}

        for group in groups_response:
            new_group = {}
            for version_raw in group['versions']:
                version = version_raw['version']
                preferred = version_raw == group['preferredVersion']
                new_group[version] = self.get_resources_for_apiversion(prefix, group['name'], version, preferred)
            groups[prefix][group['name']] = new_group
        return groups

    def get_resources_for_apiversion(self, prefix, group, version, preferred):
        """ returns a dictionary of resources associated with provided groupVersion"""

        resources = {}

        path = '/'.join(filter(None, [prefix, group, version]))
        resources_response = self.request('GET', path)['resources']

        # TODO: Filter out subresources for now
        resources_raw = filter(lambda resource: '/' not in resource['name'], resources_response)

        for resource in resources_raw:
            resources[resource['kind']] = Resource(
                prefix=prefix,
                group=group,
                apiversion=version,
                client=self,
                preferred=preferred,
                **resource
            )
        return resources

    def list(self, resource, namespace=None):
        path_params = {}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_base']
            path_params['namespace'] = namespace
        else:
            resource_path = resource.urls['base']
        return ResourceInstance(resource, self.request('get', resource_path, path_params=path_params))

    def get(self, resource, name=None, namespace=None):
        if name is None:
            return self.list(resource, namespace=namespace)
        path_params = {'name': name}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_full']
            path_params['namespace'] = namespace
        else:
            resource_path = resource.urls['full']
        return ResourceInstance(resource, self.request('get', resource_path, path_params=path_params))

    def create(self, resource, body, namespace=None):
        path_params = {}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_base']
            path_params['namespace'] = namespace
        elif resource.namespaced and not namespace:
            if body.get('metadata') and body['metadata'].get('namespace'):
                resource_path = resource.urls['namespaced_base']
                path_params['namespace'] = body['metadata']['namespace']
        else:
            resource_path = resource.urls['base']
        return ResourceInstance(resource, self.request('post', resource_path, path_params=path_params, body=body))

    def delete(self, resource, name, namespace=None):
        path_params = {'name': name}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_full']
            path_params['namespace'] = namespace
        else:
            resource_path = resource.urls['full']
        return ResourceInstance(resource, self.request('delete', resource_path, path_params=path_params))

    def replace(self, resource, body, name=None, namespace=None):
        if name is None:
            name = body['metadata']['name']
        path_params = {'name': name}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_full']
            path_params['namespace'] = namespace
        elif resource.namespaced and not namespace:
            if body.get('metadata') and body['metadata'].get('namespace'):
                resource_path = resource.urls['namespaced_full']
                path_params['namespace'] = body['metadata']['namespace']
        else:
            resource_path = resource.urls['full']

        return ResourceInstance(resource, self.request('put', resource_path, path_params=path_params, body=body))

    def update(self, resource, body, name=None, namespace=None):
        if name is None:
            name = body['metadata']['name']
        path_params = {'name': name}
        if resource.namespaced and namespace:
            resource_path = resource.urls['namespaced_full']
            path_params['namespace'] = namespace
        elif resource.namespaced and not namespace:
            if body.get('metadata') and body['metadata'].get('namespace'):
                resource_path = resource.urls['namespaced_full']
                path_params['namespace'] = body['metadata']['namespace']
        else:
            resource_path = resource.urls['full']
        content_type = self.client.\
            select_header_content_type(['application/json-patch+json', 'application/merge-patch+json', 'application/strategic-merge-patch+json'])

        return ResourceInstance(resource, self.request('patch', resource_path, path_params=path_params, body=body, content_type=content_type))

    def request(self, method, path, body=None, **params):

        if not path.startswith('/'):
            path = '/' + path

        path_params = params.get('path_params', {})
        query_params = []
        if 'pretty' in params:
            query_params.append(('pretty', params['pretty']))
        header_params = {}
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

        return json.loads(self.client.call_api(
            path,
            method.upper(),
            path_params,
            query_params,
            header_params,
            body=body,
            post_params=form_params,
            files=local_var_files,
            auth_settings=auth_settings,
            _preload_content=False
        )[0].data)


class Resource(object):

    def __init__(self, prefix=None, group=None, apiversion=None, kind=None,
                 namespaced=False, verbs=None, name=None, preferred=False, client=None,
                 singularName=None, shortNames=None, categories=None, **kwargs):

        if None in (apiversion, kind, prefix):
            raise Exception("At least prefix, kind, and apiversion must be provided")

        self.prefix = prefix
        self.group = group
        self.apiversion = apiversion
        self.kind = kind
        self.namespaced = namespaced
        self.verbs = verbs
        self.name = name
        self.preferred = preferred
        self.client = client
        self.singular_name = singularName
        self.short_names = shortNames
        self.categories = categories

        self.extra_args = kwargs

    def __repr__(self):
        if self.group:
            groupversion = '{}/{}'.format(self.group, self.apiversion)
        else:
            groupversion = self.apiversion
        return '<{}({}.{}>)'.format(self.__class__.__name__, groupversion, self.kind)

    @property
    def urls(self):
        if self.group:
            full_prefix = '{}/{}/{}'.format(self.prefix, self.group, self.apiversion)
        else:
            full_prefix = '{}/{}'.format(self.prefix, self.apiversion)
        return {
            'base': '/{}/{}'.format(full_prefix, self.name),
            'namespaced_base': '/{}/namespaces/{{namespace}}/{}'.format(full_prefix, self.name),
            'full': '/{}/{}/{{name}}'.format(full_prefix, self.name),
            'namespaced_full': '/{}/namespaces/{{namespace}}/{}/{{name}}'.format(full_prefix, self.name)
        }

    def __getattr__(self, name):
        return partial(getattr(self.client, name), self)


class ResourceContainer(object):
    def __init__(self, resources):
        self.__resources = resources

    def get(self, **kwargs):
        results = self.search(**kwargs)
        if len(results) == 1:
            return results[0]
        elif not results:
            raise Exception('No matches found for {}'.format(kwargs))
        else:
            raise Exception('Multiple matches found for {}: {}'.format(kwargs, results))

    def search(self, **kwargs):
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

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __repr__(self):
        return pformat(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __getitem__(self, name):
        return self.__dict__[name]

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__.keys())


class ResourceInstance(object):

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
        ret[key] = {k: v for k, v in resource.__dict__.items() if k != 'client'}

    print(yaml.safe_dump(ret))
    return 0


if __name__ == '__main__':
    sys.exit(main())
