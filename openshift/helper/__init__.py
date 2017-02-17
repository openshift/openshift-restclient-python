# -*- coding: utf-8 -*-

import inspect
import re

import string_utils

from kubernetes import config
from kubernetes.client.rest import ApiException
from openshift import client
from openshift.client.models import V1DeleteOptions

# Regex for finding versions
VERSION_RX = re.compile("V\d((alpha|beta)\d)?")

# Expected metaclass object name
METACLASS_NAME = 'V1ObjectMeta'


class OpenShiftException(Exception):
    """
    Raised when there is an error inside of an Ansible module.
    """

    def __init__(self, message, **kwargs):
        """
        Creates an instance of the AnsibleModuleError class.
        :param message: The friendly error message.
        :type message: basestring
        :param kwargs: All other keyword arguments.
        :type kwargs: dict
        """
        self.message = message
        self.value = kwargs
        self.value['message'] = message

    def __str__(self):
        """
        String representation of the instance.
        """
        return json.dumps(self.value)


class KubernetesObjectHelper(object):
    # TODO: add support for check mode to helper
    def __init__(self, api_version, kind, namespaced=False):
        self.api_version = api_version
        self.kind = kind
        self.model = self.__get_model(api_version, kind)
        self.properties = self.properties_from_model_obj(self.model())
        self.namespaced = namespaced

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
            if prop_kind in 'str':
                prop_class = str
            elif prop_kind == 'int':
                prop_class = int
            elif prop_kind.startswith('list['):
                prop_class = list
            elif prop_kind.startswith('dict('):
                prop_class = dict
            elif prop_kind == 'bool':
                prop_class = bool
            else:
                prop_class = getattr(client.models, prop_kind)
            # cls.properties_from_model_obj(())
            properties[name] = prop_class
        return properties

    def __lookup_method(self, operation, namespaced):
        '''

        :param operation:
        :param namespaced:
        :return:
        '''
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
        '''
        Return the model class for the requested object.

        :param api_version: API version string
        :param kind: The name of object type (i.e. Service, Route, Container, etc.)
        :return: class
        '''
        camel_kind = string_utils.snake_case_to_camel(kind).capitalize()
        model_name = api_version.capitalize() + camel_kind
        model = getattr(client.models, model_name)
        return model

    @property
    def argspec(self):
        '''
        Introspect the model properties, and return an Ansible module arg_spec dict.

        :return: dict
        '''
        argument_spec = {
            'state': {
                'default': 'present',
                'choices': ['present', 'absent']
            },
            'name': {
                'required': True
            },
            # path to a config file
            'kubeconfig': {},

            # kubectl context name
            'context': {}
        }

        if 'metadata' not in self.properties.keys():
            raise OpenShiftException(
                "Object {} does not contain metadata field".format(self.model)
            )

        if self.namespaced:
            argument_spec['namespace'] = {'required': True}

        # mutually_exclusive = None
        # required_together = None
        # required_one_of = None
        # required_if = None

        argument_spec.update(self.__transform_properties(self.properties))
        return argument_spec

    def __transform_properties(self, properties, prefix=None):
        '''
        Convert a list of properties to an argument_spec dictionary

        :param properties: List of properties from self.properties_from_model_obj()
        :param prefix: String to prefix to argument names.
        :return: dict
        '''
        args = {}
        print("here!")
        for prop, prop_class in properties.items():
            print("property: {}".format(prop))
            if prop == 'status':
                # Do not expose Status to argument spec
                continue
            elif prop == 'metadata':
                # Filter metadata properties added to argument spec
                if prop_class.__name__ != METACLASS_NAME:
                    raise OpenShiftException("Unknown metadata type: {}".format(prop_class.__name__))
                args['labels'] = {'required': False, 'type': 'dict'}
                args['annotations'] = {'required': False, 'type': 'dict'}
            elif prop_class.__name__ not in ['int', 'str', 'bool', 'list', 'dict']:
                # Adds nested properties
                p = prefix
                if prop not in ('spec', 'template'):
                    # Only prefix property names with meaningful terms
                    p = prefix + '_' if prefix else ''
                    p += prop
                sub_props = self.properties_from_model_obj(prop_class())
                args.update(self.__transform_properties(sub_props, prefix=p))
            else:
                # Adds a primitive property
                arg_prefix = prefix + '_' if prefix else ''
                args[arg_prefix + prop] = { 'required': False, 'type': prop_class.__name__}
        return args
