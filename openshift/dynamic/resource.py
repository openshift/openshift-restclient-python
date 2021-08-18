from kubernetes.dynamic.resource import Resource, Subresource, ResourceField  # noqa


class ResourceList(Resource):
    """ Represents a list of API objects """

    def __init__(self, client, group='', api_version='v1', base_kind='', kind=None, base_resource_lookup=None):
        self.client = client
        self.group = group
        self.api_version = api_version
        self.kind = kind or '{}List'.format(base_kind)
        self.base_kind = base_kind
        self.base_resource_lookup = base_resource_lookup
        self.__base_resource = None

    def base_resource(self):
        if self.__base_resource:
            return self.__base_resource
        elif self.base_resource_lookup:
            self.__base_resource = self.client.resources.get(**self.base_resource_lookup)
            return self.__base_resource
        return None

    def apply(self, *args, **kwargs):
        return self.verb_mapper('apply', *args, **kwargs)

    def to_dict(self):
        return {
            '_type': 'ResourceList',
            'group': self.group,
            'api_version': self.api_version,
            'kind': self.kind,
            'base_kind': self.base_kind,
            'base_resource_lookup': self.base_resource_lookup
        }

    def __getattr__(self, name):
        if self.base_resource():
            return getattr(self.base_resource(), name)
        return None


class ResourceInstance(object):
    """ A parsed instance of an API resource. It exists solely to
        ease interaction with API objects by allowing attributes to
        be accessed with '.' notation.
    """

    def __init__(self, client, instance):
        self.client = client
        # If we have a list of resources, then set the apiVersion and kind of
        # each resource in 'items'
        kind = instance['kind']
        if kind.endswith('List') and 'items' in instance:
            kind = instance['kind'][:-4]
            if instance['items']:
                for item in instance['items']:
                    if 'apiVersion' not in item:
                        item['apiVersion'] = instance['apiVersion']
                    if 'kind' not in item:
                        item['kind'] = kind

        self.attributes = self.__deserialize(instance)
        self.__initialised = True
