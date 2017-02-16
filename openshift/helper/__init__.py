import inspect
import re

import string_utils

from kubernetes import config
from kubernetes.client.rest import ApiException
from openshift import client
from openshift.client.models import V1DeleteOptions

#: Regex for finding versions
VERSION_RX = re.compile("V\d((alpha|beta)\d)?")


class KubernetesObjectHelper(object):
    # TODO: add support for check mode to helper
    def __init__(self, api_version, kind):
        self.api_version = api_version
        self.kind = kind
        self.model = self.__get_model(api_version, kind)

        model_obj = self.model()
        self.properties = self.properties_from_model_obj(model_obj)

        # TODO: handle config better than just using default kubeconfig
        config.load_kube_config()

    def get_object(self, name, namespace=None):
        # TODO: better error handling
        k8s_obj = None
        try:
            if namespace is None:
                get_method = self.__lookup_method('read', False)
                k8s_obj = get_method(name)
            else:
                get_method = self.__lookup_method('read', True)
                k8s_obj = get_method(name, namespace)
        except ApiException as e:
            if e.status != 404:
                raise
        return k8s_obj

    def patch_object(self, name, namespace, k8s_obj):
        # TODO: better error handling
        # TODO: add a parameter for waiting until the object is ready
        k8s_obj.status = None
        k8s_obj.metadata.resource_version = None
        if namespace is None:
            patch_method = self.__lookup_method('patch', False)
            return_obj = patch_method(name, k8s_obj)
        else:
            patch_method = self.__lookup_method('patch', True)
            return_obj = patch_method(name, namespace, k8s_obj)
        return return_obj

    def create_object(self, namespace, k8s_obj):
        # TODO: better error handling
        # TODO: add a parameter for waiting until the object is ready
        if namespace is None:
            create_method = self.__lookup_method('create', False)
            return_obj = create_method(k8s_obj)
        else:
            create_method = self.__lookup_method('create', True)
            return_obj = create_method(namespace, k8s_obj)
        return return_obj

    def delete_object(self, name, namespace=None, delete_opts=None):
        # TODO: better error handling
        # TODO: add a parameter for waiting until the object has been deleted
        # TODO: deleting a namespace requires a body
        if namespace is None:
            delete_method = self.__lookup_method('delete', False)
            print(inspect.getargspec(delete_method))
            if 'body' in inspect.getargspec(delete_method).args:
                delete_method(name, body=V1DeleteOptions())
            else:
                delete_method(name)
        else:
            delete_method = self.__lookup_method('delete', True)
            if 'body' in inspect.getargspec(delete_method).args:
                delete_method(name, namespace, body=V1DeleteOptions())
            else:
                delete_method(name, namespace)

    @classmethod
    def properties_from_model_obj(cls, model_obj):
        model_class = type(model_obj)
        property_names = [
            x for x in dir(model_class)
            if isinstance(getattr(model_class, x), property)
        ]
        properties = {}
        for name in property_names:
            prop_kind = model_obj.swagger_types[name]
            if prop_kind == 'str':
                prop_class = str
            elif prop_kind == 'int':
                prop_class = int
            elif prop_kind.startswith('list['):
                prop_class = list
            elif prop_kind.startswith('dict('):
                prop_class = dict
            else:
                prop_class = getattr(client.models, prop_kind)

            properties[name] = prop_class
        return properties

    def __lookup_method(self, operation, namespaced):
        # TODO: raise error if method not found
        method_name = operation
        if namespaced:
            method_name += '_namespaced'
        method_name += '_' + self.kind

        apis = [x for x in dir(client.apis) if VERSION_RX.search(x)]
        apis.append('OapiApi')

        method = None

        for api in apis:
            api_class = getattr(client.apis, api)
            method = getattr(api_class(), method_name, None)
            if method is not None:
                break

        return method

    @staticmethod
    def __get_model(api_version, kind):
        camel_kind = string_utils.snake_case_to_camel(kind).capitalize()
        model_name = api_version.capitalize() + camel_kind
        model = getattr(client.models, model_name)
        return model
