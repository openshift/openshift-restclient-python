# -*- coding: utf-8 -*-
from __future__ import absolute_import

import copy
import json
import logging
import re
import string_utils

from openshift.client import models

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
                'choices': ['present', 'absent', 'replaced'],
                'description': [
                    "Determines if the object should be created, patched, deleted or replaced. When set to "
                    "C(present), the object will be created, if it does not exist, or patched, if requested "
                    "parameters differ from existing object attributes. If set to C(absent), an existing "
                    "object will be deleted, and if set to C(replaced), an existing object will be completely "
                    "replaced with a new object created from the supplied parameters."
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
        logger.debug(self.__log_argspec())
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
            spec = self.find_arg_spec(param_name)
            if spec.get('property_path'):
                prop_path = copy.copy(spec['property_path'])
                self.__set_obj_attribute(obj, prop_path, param_value, param_name)
        logger.debug("Object from params:")
        logger.debug(json.dumps(obj.to_dict(), indent=4))
        return obj

    def find_arg_spec(self, module_param_name):
        """For testing, allow the param_name value to be an alias"""
        if self.argspec.get(module_param_name):
            return self.argspec[module_param_name]
        result = None
        for key, value in self.argspec.items():
            if value.get('aliases'):
                for alias in value['aliases']:
                    if alias == module_param_name:
                        result = self.argspec[key]
                        break
                if result:
                    break
        if not result:
            raise OpenShiftException(
                "Error: received unrecognized module parameter {}".format(module_param_name)
            )
        return result

    def __set_obj_attribute(self, obj, property_path, param_value, param_name):
        """
        Recursively set object properties
        :param obj: The object on which to set a property value.
        :param property_path: A list of property names in the form of strings.
        :param param_value: The value to set.
        :return: The original object.
        """
        logger.debug("set_obj_attribute {0}, {1} to {2}".format(obj.__class__.__name__,
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
                    self.__compare_dict(getattr(obj, prop_name), param_value, param_name)
            elif prop_kind.startswith('list['):
                if getattr(obj, prop_name) is None:
                    setattr(obj, prop_name, [])
                obj_type = prop_kind.replace('list[', '').replace(']','')
                if obj_type not in ('str', 'int', 'bool', 'list', 'dict'):
                    self.__compare_obj_list(getattr(obj, prop_name), param_value, obj_type, param_name)
                else:
                    self.__compare_list(getattr(obj, prop_name), param_value, param_name)
            else:
                # prop_kind is an object class
                sub_obj = getattr(obj, prop_name)
                if not sub_obj:
                    sub_obj = getattr(models, prop_kind)()
                setattr(obj, prop_name, self.__set_obj_attribute(sub_obj, property_path, param_value, param_name))
        return obj

    @staticmethod
    def __compare_list(src_values, request_values, param_name):
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
                    if '__cmp__' in dir(src_dict):
                        # python < 3
                        if src_dict >= request_dict:
                            match = True
                            break
                    elif src_dict.items() == request_dict.items():
                        # python >= 3
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
                "Evaluating {0}: encountered unimplemented type {1} in "
                "__compare_list()".format(param_name, type(src_values[0]).__name__)
            )

    def __compare_dict(self, src_value, request_value, param_name):
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
                self.__compare_list(src_value[item], value, param_name)
            elif type(value).__name__ == 'dict':
                self.__compare_dict(src_value[item], value, param_name)
            else:
                raise OpenShiftException(
                    "Evaluating {0}: encountered unimplemented type {1} in "
                    "__compare_dict()".format(param_name, type(value).__name__)
                )

    def __compare_obj_list(self, src_value, request_value, obj_class, param_name):
        """
        Compare a src_value (list of ojects) with a request_value (list of dicts), and update
        src_value with differences. Assumes each object and each dict has a 'name' attributes,
        which can be used for matching. Elements are not removed from the src_value list.
        """
        sample_obj = getattr(models, obj_class)()

        # Try to determine the unique key for the array
        key_names = [
            'name',
            'type'
        ]
        key_name = None
        for key in key_names:
            if hasattr(sample_obj, key):
                key_name = key
                break

        if key_name and request_value[0].get(key_name):
            # compare by key field
            for item in request_value:
                if not item.get(key_name):
                    logger.debug("FAILED on: {}".format(item))
                    raise OpenShiftException(
                        "Evaluating {0} - expecting dict to contain a `{1}` attribute "
                        "in __compare_obj_list()  for model {2}.".format(param_name,
                                                                         key_name,
                                                                         self.get_base_model_name_snake(obj_class))
                    )
                found = False
                for obj in src_value:
                    if not obj:
                        continue
                    if getattr(obj, key_name) == item[key_name]:
                        # Assuming both the src_value and the request value include a name property
                        found = True
                        for key, value in item.items():
                            item_kind = sample_obj.swagger_types.get(key)
                            if item_kind in ('str', 'bool', 'int') or type(value).__name__ in ('str', 'int', 'bool'):
                                setattr(obj, key, value)
                            elif item_kind.startswith('list['):
                                obj_type = item_kind.replace('list[', '').replace(']', '')
                                if obj_type not in ('str', 'int', 'bool'):
                                    self.__compare_obj_list(getattr(obj, key), value, obj_type, param_name)
                                else:
                                    # Straight list comparison
                                    self.__compare_list(getattr(obj, key), value, param_name)
                            elif item_kind.startswith('dict('):
                                self.__compare_dict(getattr(obj, key), value, param_name)
                            elif item_kind.endswith('Params') and type(value).__name__ == 'dict':
                                # parameter object
                                param_obj = getattr(obj, key)
                                if not param_obj:
                                    setattr(obj, key, getattr(models, item_kind)())
                                    param_obj = getattr(obj, key)
                                self.__update_object_properties(param_obj, value)
                            else:
                                raise OpenShiftException(
                                    "Evaluating {0}: encountered unimplemented type {1} in "
                                    "__compare_obj_list() for model {2}".format(param_name,
                                                                                item_kind,
                                                                                self.get_base_model_name_snake(obj_class))
                                )
                if not found:
                    src_value.append(
                        self.__update_object_properties(getattr(models, obj_class)(), item)
                    )
        else:
            # There isn't a key, or we don't know what it is, so check for all properties to match
            for item in request_value:
                found = False
                for obj in src_value:
                    match = True
                    for item_key, item_value in item.items():
                        # TODO: this should probably take the property type into account
                        if getattr(obj, item_key) != item_value:
                            match = False
                            break
                    if match:
                        found = True
                        break
                if not found:
                    src_value.append(
                        self.__update_object_properties(getattr(models, obj_class)(), item)
                    )

    def __update_object_properties(self, obj, item):
        """ Recursively update an object's properties. Returns a pointer to the object. """
        for key, value in item.items():
            try:
                kind = obj.swagger_types[key]
            except:
                possible_matches = ', '.join(list(obj.swagger_types.keys()))
                class_snake_name = self.get_base_model_name_snake(type(obj).__name__)
                raise OpenShiftException(
                    "Unable to find '{0}' in {1}. Valid property names include: {2}".format(key,
                                                                                            class_snake_name,
                                                                                            possible_matches)
                )
            if kind in ('str', 'int', 'bool') or kind.startswith('list[') or kind.startswith('dict('):
                self.__set_obj_attribute(obj, [key], value, key)
            elif type(value).__name__ != 'dict':
                # likely hit IntstrIntOrString
                setattr(obj, key, value)
            else:
                # kind is an object, hopefully
                if not getattr(obj, key):
                    setattr(obj, key, getattr(models, kind)())
                self.__update_object_properties(getattr(obj, key), value)

        return obj

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

    @staticmethod
    def __convert_params_to_choices(properties):
        def snake_case(name):
            result = string_utils.snake_case_to_camel(name.replace('_params', ''))
            return result[:1].capitalize() + result[1:]
        return [snake_case(x) for x in list(properties.keys()) if x.endswith('params')]

    def __transform_properties(self, properties, prefix='', path=None, alternate_prefix='', hidden=False):
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

        def add_meta(prop_name, prop_prefix, prop_alt_prefix):
            """ Adds metadata properties to the argspec """
            if prop_alt_prefix:
                args[prop_prefix + prop_name]['aliases'] = [prop_alt_prefix + prop_name]
            elif prop_prefix:
                args[prop_prefix + prop_name]['aliases'] = [prop_name]
            prop_paths = copy.copy(path)  # copy path from outer scope
            prop_paths.append('metadata')
            prop_paths.append(prop_name)
            args[prop_prefix + prop_name]['property_path'] = prop_paths
            if hidden:
                args[prop_prefix + prop_name]['hide_from_module'] = True

        for prop, prop_attributes in properties.items():
            if prop in ('api_version', 'status', 'kind'):
                # Don't expose these properties
                continue
            elif prop_attributes['immutable']:
                # Property cannot be set by the user
                continue
            elif prop == 'metadata':
                meta_prefix = prefix + '_metadata_' if prefix else ''
                meta_alt_prefix = alternate_prefix + '_metadata_' if alternate_prefix else ''
                if 'labels' in dir(prop_attributes['class']):
                    args[meta_prefix + 'labels'] = {
                        'type': 'dict',
                    }
                    add_meta('labels', meta_prefix, meta_alt_prefix)
                if 'annotations' in dir(prop_attributes['class']):
                    args[meta_prefix + 'annotations'] = {
                        'type': 'dict',
                    }
                    add_meta('annotations', meta_prefix, meta_alt_prefix)
                if 'namespace' in dir(prop_attributes['class']):
                    args[meta_prefix + 'namespace'] = {}
                    add_meta('namespace', meta_prefix, meta_alt_prefix)
                if 'name' in dir(prop_attributes['class']):
                    args[meta_prefix + 'name'] = {
                        'required': True,
                    }
                    add_meta('name', meta_prefix, meta_alt_prefix)
            elif prop_attributes['class'].__name__ not in ['int', 'str', 'bool', 'list', 'dict']:
                # Adds nested properties recursively

                # As we traverse deeper into nested properties, we prefix the final primitive property name with the
                # chain of property names. For example, 'pod_pod_security_context_run_as_user', where 'run_as_user' is
                # the primitive.
                #
                # This may be too hacky, but trying to remove redundant prefixes and generic, non-helpful
                # prefixes (e.g. Spec, Template).
                label = prop_attributes['class'].__name__\
                        .replace(self.base_model_name, '')\
                        .replace(self.api_version.capitalize(), '')\
                        .replace(BASE_API_VERSION, '')\
                        .replace('Unversioned', '')

                # Provide a more human-friendly version of the prefix
                alternate_label = label\
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
                sub_is_hidden = hidden
                if prop.endswith('params') and 'type' in properties:
                    # If the object contains a 'type' field (e.g. v1_deployment_trigger_policy),
                    # then '_params' objects should not be picked up by the Ansible module.
                    sub_is_hidden = True
                sub_props = self.properties_from_model_obj(prop_attributes['class']())
                args.update(self.__transform_properties(sub_props, prefix=p, path=paths, alternate_prefix=a,
                                                        hidden=sub_is_hidden))
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

                if hidden:
                    args[arg_prefix + prop]['hide_from_module'] = True

                # Use the alternate prefix to construct a human-friendly alias
                if arg_alt_prefix:
                    args[arg_prefix + prop]['aliases'] = [arg_alt_prefix + prop]
                elif arg_prefix:
                    args[arg_prefix + prop]['aliases'] = [prop]

                if prop == 'type':
                    args[arg_prefix + prop]['choices'] = self.__convert_params_to_choices(properties)
        return args

