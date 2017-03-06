# -*- coding: utf-8 -*-
from __future__ import absolute_import

import copy
import json
import logging
import re
import string_utils

from openshift import client

from . import KubernetesObjectHelper, BASE_API_VERSION
from .exceptions import OpenShiftException

# Attributes in argspec not needed by Ansible
ARG_ATTRIBUTES_BLACKLIST = ('description', 'auth_option', 'property_path')

logger = logging.getLogger(__name__)


class AnsibleModuleHelper(KubernetesObjectHelper):
    _argspec_cache = None

    @property
    def argspec(self):
        """
        Introspect the model properties, and return an Ansible module arg_spec dict.

        :return: dict
        """
        if self._argspec_cache:
            return self._argspec_cache

        argument_spec = {
            # path to kube config file
            'state': {
                'default': 'present',
                'choices': ['present', 'absent'],
                'description': [
                    "Determines if the object should be created, patched or deleted. When set to C(present), "
                    "the object will be created, if it does not exist, or patched, if requested parameters "
                    "differ from existing object attributes. Set to C(absent) to delete an existing object."
                ]
            },
            'kubeconfig': {
                'type': 'path',
                'description': [
                    "Path to an existing Kubernetes config file. If not provided, and no other connection "
                    "options are provided, the openshift client will attempt to load the default configuration "
                    "file from I(~/.kube/config.json)."
                ]},

            # kubectl context name
            'context': {
                'description': [
                    "The name of a context found in the Kubernetes config file."
                ]
            },

            # authentication settings
            'api_url': {
                'auth_option': True,
                'description': ["Provide a URL for acessing the Kubernetes API."]
            },
            'api_key': {
                'auth_option': True,
                'no_log': True,
                'description': ["Token used to connect to the API."]
            },
            'username': {
                'auth_option': True,
                'description': [
                    "Provide a username for connecting to the API."
                ]
            },
            'password': {
                'auth_option': True,
                'no_log': True,
                'description': [
                    "Provide a password for connecting to the API. Use in conjunction with I(username)."
                ]
            },
            'verify_ssl': {
                'default': True,
                'type': 'bool',
                'auth_option': True,
                'description': [
                    "Whether or not to verify the API server's SSL certificates."
                ]
            },
            'ssl_ca_cert': {
                'type': 'path',
                'auth_option': True,
                'description': [
                    "Path to a CA certificate used to authenticate with the API."
                ]
            },
            'cert_file': {
                'type': 'path',
                'auth_option': True,
                'description': [
                    "Path to a certificate used to authenticate with the API."
                ]
            },
            'key_file': {
                'type': 'path',
                'auth_option': True,
                'description': [
                    "Path to a key file used to authenticate with the API."
                ]
            },
            'debug': {
                'type': 'bool',
                'default': False,
                'description': [
                    "Enable debug output from the OpenShift helper. Logging info is written "
                    "to KubeObjHelper.log"
                ]
            }
        }

        argument_spec.update(self.__transform_properties(self.properties))

        if re.search(r'list$', self.base_model_name_snake) and argument_spec.get('items'):
            # Lists are read only, so having a 'state' option doesn't make sense
            argument_spec.pop('state')

        self._argspec_cache = argument_spec
        return self._argspec_cache

    def object_from_params(self, module_params, obj=None):
        """
        Update a model object with Ansible module param values. Optionally pass an object
        to update, otherwise a new object will be created.
        :param module_params: dict of key:value pairs
        :param obj: model object to update
        :return: updated model object
        """
        if not obj:
            obj = self.model()
            camel_kind = string_utils.snake_case_to_camel(self.kind)
            obj.kind = camel_kind[:1].capitalize() + camel_kind[1:]
            obj.api_version = self.api_version.lower()
        for param_name, param_value in module_params.items():
            if self.argspec[param_name].get('property_path'):
                spec = self.argspec[param_name]
                prop_path = copy.copy(spec['property_path'])
                self.__set_obj_attribute(obj, prop_path, param_value)
        logger.debug("Object from params:")
        logger.debug(json.dumps(obj.to_dict(), indent=4))
        return obj

    def __set_obj_attribute(self, obj, property_path, param_value):
        """
        Recursively set object properties
        :param obj: The object on which to set a property value.
        :param property_path: A list of property names in the form of strings.
        :param param_value: The value to set.
        :return: The original object.
        """
        logger.debug("set {0}, {1} to {2}".format(obj.__class__.__name__,
                                                  json.dumps(property_path),
                                                  json.dumps(param_value)))
        while len(property_path) > 0:
            prop_name = property_path.pop(0)
            prop_kind = obj.swagger_types[prop_name]
            if prop_kind in ('str', 'int', 'bool'):
                # prop_kind is a primitive
                setattr(obj, prop_name, param_value)
            elif prop_kind.startswith('dict('):
                if not getattr(obj, prop_name):
                    setattr(obj, prop_name, param_value)
                else:
                    self.__compare_dict(getattr(obj, prop_name), param_value)
            elif prop_kind.startswith('list['):
                if getattr(obj, prop_name) is None:
                    setattr(obj, prop_name, [])
                logger.debug("prop.kind: {}".format(prop_kind))
                obj_type = prop_kind.replace('list[', '').replace(']','')
                if obj_type not in ('str', 'int', 'bool', 'list', 'dict'):
                    self.__compare_obj_list(getattr(obj, prop_name), param_value, obj_type)
                else:
                    self.__compare_list(getattr(obj, prop_name), param_value)
            else:
                # prop_kind is an object class
                sub_obj = getattr(obj, prop_name)
                if not sub_obj:
                    sub_obj = getattr(client.models, prop_kind)()
                    logger.debug("sub_obj is {}".format(sub_obj.__class__.__name__))
                logger.debug("set {0}.{1}".format(obj.__class__.__name__, prop_name))
                setattr(obj, prop_name, self.__set_obj_attribute(sub_obj, property_path, param_value))
        return obj

    @staticmethod
    def __compare_list(src_values, request_values):
        """
        Compare src_values list with request_values list, and ppend any missing
        request_values to src_values.
        """
        if not request_values:
            return

        if not src_values:
            src_values += request_values

        if type(src_values[0]).__name__ in ('str', 'int', 'bool'):
            # lists contain primitive types
            if set(src_values) >= set(request_values):
                # src_value list includes request_value list
                return
            # append the missing elements from request value
            src_values += list(set(request_values) - set(src_values))
        elif type(src_values[0]).__name__ == 'dict':
            missing = []
            for request_dict in request_values:
                match = False
                for src_dict in src_values:
                    if src_dict.items() == request_dict.items():
                        match = True
                        break
                if not match:
                    missing.append(request_dict)
            src_values += missing
        elif type(src_values[0]).__name__ == 'list':
            missing = []
            for request_list in request_values:
                match = False
                for src_list in src_values:
                    if set(request_list) >= set(src_list):
                        match = True
                        break
                if not match:
                    missing.append(request_list)
            src_values += missing
        else:
            raise OpenShiftException(
                "__compare_list: Encountered unimplemented type {0}".format(type(src_values[0]).__name__)
            )

    def __compare_dict(self, src_value, request_value):
        """
        Compare src_value dict with request_value dict, and update src_value with any differences.
        Does not remove items from src_value dict.
        """
        if not request_value:
            return
        for item, value in request_value.items():
            if type(value).__name__ in ('str', 'int', 'bool'):
                src_value[item] = value
            elif type(value).__name__ == 'list':
                self.__compare_list(src_value[item], value)
            elif type(value).__name__ == 'dict':
                self.__compare_dict(src_value[item], value)
            else:
                raise OpenShiftException(
                    "__compare_dict: Encountered unimplemented type {0}".format(type(value).__name__)
                )

    def __compare_obj_list(self, src_value, request_value, obj_class):
        """
        Compare a src_value (list of ojects) with a request_value (list of dicts), and update
        src_value with differences. Assumes each object and each dict has a 'name' attributes,
        which can be used for matching. Elements are not removed from the src_value list.
        """
        sample_obj = getattr(client.models, obj_class)()
        for item in request_value:
            if item is None:
                continue
            if not item.get('name'):
                raise OpenShiftException(
                    "Error: Expecting dict for {0} to contain a `name` attribute."
                )
            found = False
            for obj in src_value:
                if obj.name == item['name']:
                    # Assuming both the src_value and the request value include a name property
                    found = True
                    for key, value in item.items():
                        if type(value).__name__ in ('str', 'bool', 'int'):
                            if value != getattr(obj, key):
                                setattr(obj, key, value)
                        elif type(value).__name__ == 'list':
                            if hasattr(sample_obj, 'swagger_types') and sample_obj.swagger_types.get(key):
                                # compare the requested list, which should be a list of dicts to a list of objects
                                obj_type = sample_obj.swagger_types.get(key).replace('list[', '').replace(']', '')
                                self.__compare_obj_list(getattr(obj, key), value, obj_type)
                            else:
                                # Straight list comparison
                                self.__compare_list(getattr(obj, key), value)
                        elif type(value).__name__ == 'dict':
                            self.__compare_dict(getattr(obj, key), value)
                        else:
                            raise OpenShiftException(
                                "__compare_obj_list: In model {0} encountered unimplemented type {0}"
                                .format(self.get_base_model_name_snake(obj_class), type(value).__name__)
                            )
            if not found:
                # No matching name found. Add a new instance to the list.
                for key, value in item.items():
                    setattr(sample_obj, key, value)
                    src_value.append(sample_obj)

    def __log_argspec(self):
        """
        Safely logs the argspec by not including any params with the no_log attribute.

        :return: None
        """
        logger.debug("arg_spec:")
        tmp_arg_spec = copy.deepcopy(self.argspec)
        pop_keys = []
        for key, value in tmp_arg_spec.items():
            if value.get('no_log'):
                pop_keys.append(key)
        for key in pop_keys:
            tmp_arg_spec.pop(key)
        logger.debug(json.dumps(tmp_arg_spec, indent=4, sort_keys=True))

    def __transform_properties(self, properties, prefix='', path=None, alternate_prefix=''):
        """
        Convert a list of properties to an argument_spec dictionary

        :param properties: List of properties from self.properties_from_model_obj()
        :param prefix: String to prefix to argument names.
        :param path: List of property names providing the recursive path through the model to the property
        :param alternate_prefix: a more minimal version of prefix
        :return: dict
        """
        if path is None:
            path = []

        args = {}
        for prop, prop_attributes in properties.items():
            if prop in ('api_version', 'status', 'kind'):
                # Don't expose these properties
                continue
            elif prop_attributes['immutable']:
                # Property cannot be set by the user
                continue
            elif prop == 'metadata':
                if 'labels' in dir(prop_attributes['class']):
                    args['labels'] = {
                        'type': 'dict',
                        'property_path': ['metadata', 'labels'],
                        'aliases': ['metadata_labels']
                    }
                if 'annotations' in dir(prop_attributes['class']):
                    args['annotations'] = {
                        'type': 'dict',
                        'property_path': ['metadata', 'annotations'],
                        'aliases': ['metadata_aliases']
                    }
                if 'namespace' in dir(prop_attributes['class']):
                    args['namespace'] = {
                        'property_path': ['metadata', 'namespace']
                    }
                if 'name' in dir(prop_attributes['class']):
                    args['name'] = {
                        'required': True,
                        'property_path': ['metadata', 'name'],
                        'aliases': ['metadata_name']
                    }
            elif prop_attributes['class'].__name__ not in ['int', 'str', 'bool', 'list', 'dict']:
                # Adds nested properties recursively

                # As we traverse deeper into nested properties, we prefix the final primitive property name with the
                # chain of property names. For example, 'pod_pod_security_context_run_as_user', where 'run_as_user' is
                # the primitive.
                #
                # This may be too hacky, but trying to remove redundant prefixes and generic, non-helpful
                # prefixes (e.g. Spec, Template).
                label = prop_attributes['class'].__name__\
                        .replace(self.api_version.capitalize(), '')\
                        .replace(BASE_API_VERSION, '')\
                        .replace('Unversioned', '')

                # Provide a more human-friendly version of the prefix
                alternate_label = label\
                    .replace(self.base_model_name, '')\
                    .replace('Spec', '')\
                    .replace('Template', '')

                alternate_label = string_utils.camel_case_to_snake(alternate_label, '_')
                label = string_utils.camel_case_to_snake(label, '_')
                p = prefix
                a = alternate_prefix
                paths = copy.copy(path)
                paths.append(prop)

                if a:
                    # Prevent the last prefix from repeating. In other words, avoid things like 'pod_pod'
                    pieces = alternate_prefix.split('_')
                    alternate_label = alternate_label.replace(pieces[len(pieces) - 1] + '_', '', 1)
                if label != self.base_model_name and label not in p:
                    p += '_' + label if p else label
                if alternate_label != self.base_model_name and alternate_label not in a:
                    a += '_' + alternate_label if a else alternate_label
                sub_props = self.properties_from_model_obj(prop_attributes['class']())
                args.update(self.__transform_properties(sub_props, prefix=p, path=paths, alternate_prefix=a))
            else:
                # Adds a primitive property
                arg_prefix = prefix + '_' if prefix else ''
                arg_alt_prefix = alternate_prefix + '_' if alternate_prefix else ''
                paths = copy.copy(path)
                paths.append(prop)
                args[arg_prefix + prop] = {
                    'required': False,
                    'type': prop_attributes['class'].__name__,
                    'property_path': paths
                }
                # Use the alternate prefix to construct a human-friendly, alternate field name, or alias
                if arg_alt_prefix:
                    args[arg_prefix + prop]['aliases'] = [arg_alt_prefix + prop]
                elif arg_prefix:
                    args[arg_prefix + prop]['aliases'] = [prop]
        return args