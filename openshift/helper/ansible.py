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

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'AnsibleModjHelper.log',
            'mode': 'a',
            'encoding': 'utf-8'
        },
        'null': {
            'level': 'ERROR',
            'class': 'logging.NullHandler'
        }
    },
    'loggers': {
        'openshift.helper': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False
        },
    },
    'root': {
        'handlers': ['null'],
        'level': 'ERROR'
    }
}


class AnsibleModuleHelper(KubernetesObjectHelper):
    # TODO: add support for check mode to helper
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

    def object_from_params(self, module_params):
        """
        Instantiate an instance of the model class, and populate its attributes
        from the module parameters

        :param module_params: Dict of key:value pairs
        :return: The instantiated instance
        """
        obj = self.model()
        obj.kind = string_utils.snake_case_to_camel(self.kind).capitalize()
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
            if prop_kind in ('str', 'int', 'bool') or \
                    prop_kind.startswith('dict(') or \
                    prop_kind.startswith('list['):
                # prop_kind is a primitive
                setattr(obj, prop_name, param_value)
            else:
                # prop_kind is an object class
                sub_obj = getattr(obj, prop_name)
                if not sub_obj:
                    sub_obj = getattr(client.models, prop_kind)()
                    logger.debug("sub_obj is {}".format(sub_obj.__class__.__name__))
                logger.debug("set {0}.{1}".format(obj.__class__.__name__, prop_name))
                setattr(obj, prop_name, self.__set_obj_attribute(sub_obj, property_path, param_value))
        return obj

    def object_compare(self, k8s_obj, module_params):
        """
        Update an object with Ansible module params. Returns a tuple that includes a boolean and a list of
         strings. The boolean indicates if the object matched the parameters. If the object already matched
         and was not updated, the boolean is True. The list of strings provides attributes that did not match.
        :param k8s_obj:
        :param module_params: dict of Ansible module params
        :return: match, reason: match is a boolean and reason is a list of strings
        """
        match = True
        reasons = []
        logger.debug("Performing object compare")
        logger.debug("Starting object:")
        logger.debug(json.dumps(k8s_obj.to_dict(), indent=4))
        for param_name, param_value in module_params.items():
            if param_value is None:
                # nothing to do
                continue
            if not self.argspec.get(param_name, {}).get('property_path', None):
                # only interested in params that have a property_path
                continue
            parent_obj = k8s_obj
            obj_prop = k8s_obj
            prop_name = None
            for prop in self.argspec[param_name]['property_path']:
                parent_obj = obj_prop
                prop_name = prop
                obj_prop = getattr(parent_obj, prop)
            if obj_prop is None:
                reasons.append("Property {0} was null".format(param_name))
                self.__set_obj_attribute(k8s_obj,
                                         self.argspec[param_name]['property_path'],
                                         param_value)
                match = False
            elif type(obj_prop).__name__ not in ('int', 'bool', 'str', 'list', 'dict'):
                # If it's not None, then it should be a primitive
                raise OpenShiftException(
                    "Error: property_path for {0} returned a value of type {1}."
                    "Expected one of: int, bool, str, list, dict.".format(param_name, type(obj_prop).__name__)
                )
            elif type(obj_prop).__name__ in ('int', 'bool', 'str'):
                if obj_prop != module_params[param_name]:
                    reasons.append(
                        "Property {0} did not match".format(param_name)
                    )
                    self.__set_obj_attribute(k8s_obj,
                                             self.argspec[param_name]['property_path'],
                                             param_value)
                    match = False
            elif type(obj_prop).__name__ == 'list':
                if hasattr(parent_obj, 'swagger_types') and parent_obj.swagger_types.get(prop_name):
                    # compare the requested list, which should be a list of dicts to a list of objects
                    obj_type = parent_obj.swagger_types.get(prop_name).replace('list[', '').replace(']','')
                    compare_result, sub_reasons =\
                        self.compare_obj_list(obj_prop, module_params[param_name], obj_type)
                else:
                    # Straight list comparison
                    compare_result, sub_reasons = self.compare_list(obj_prop, module_params[param_name])
                if not compare_result:
                    reasons.append(
                        "Property {0} did not match: {1}".format(param_name, ', '.join(sub_reasons))
                    )
                    match = False
            elif type(obj_prop).__name__ == 'dict':
                # perform comparison and update the object property
                compare_result, sub_reasons = self.compare_dict(obj_prop, module_params[param_name])
                if not compare_result:
                    reasons.append(
                        "Property {0} did not match: {1}".format(param_name, ', '.join(sub_reasons))
                    )
                    match = False
            else:
                raise OpenShiftException(
                    "object_compare: Encountered unimplemented object type {0}".format(type(obj_prop).__name__)
                )
        logger.debug("Post object compare")
        logger.debug("Match: {}".format(match))
        logger.debug("Reasons: {}".format(json.dumps(reasons, indent=4)))
        logger.debug("Object:")
        logger.debug(json.dumps(k8s_obj.to_dict(), indent=4))
        return match, reasons

    def compare_list(self, src_value, request_value):
        """
        Compare a two lists. Returns bool indicating if they match, and a list
        of strings describing why not.
        :param src_value: A list from the existing API object.
        :param request_value: A list from request params.
        :return: match, reasons: boolean (whether or not they matched), list of strings
        """
        match = True
        reasons = []
        for item in request_value:
            if type(item).__name__ in ('str', 'int', 'bool'):
                if item in src_value:
                    continue
                reasons.append(
                    "{0} from request list not found in {1}".format(item, json.dumps(src_value))
                )
                match = False
                src_value.append(item)
            elif type(item).__name__ in ('dict', 'list'):
                match_method = getattr(self, 'compare_' + type(item).__name__)
                found_match = False
                for src_item in src_value:
                    compare_result, reason = match_method(src_item, item)
                    if compare_result:
                        found_match = True
                        break
                if not found_match:
                    reasons.append(
                        "{0} not found".format(json.dumps(item))
                    )
                    match = False
                    src_value.append(item)
            else:
                raise OpenShiftException(
                    "compare_list: Encountered unimplemented type {0}".format(type(item).__name__)
                )
        return match, reasons

    def compare_dict(self, src_value, request_value):
        """
        Compare a two dicts. Returns bool indicating if they match, and a list
        of strings describing why not.
        :param src_value: A dict from the existing API object.
        :param request_value: A dict from request params.
        :return: match, reasons: boolean (whether or not they matched), list of strings
        """
        match = True
        reasons = []
        for item, value in request_value.items():
            logger.debug('comparing item: {0} - {1}'.format(item, value))
            if src_value.get(item) == value:
                continue
            elif src_value.get(item, None) is None:
                reasons.append(
                    "key {0} not found in {1}".format(item, json.dumps(src_value))
                )
                src_value[item] = value
                match = False
            elif type(value).__name__ in ('str', 'int', 'bool') and value != src_value[item]:
                reasons.append(
                    "{0}: {1} not found in src dict {2}".format(item, value, json.dumps(src_value))
                )
                src_value[item] = value
                match = False
            elif type(value).__name__ in ('list', 'dict'):
                match_method = getattr(self, 'compare_' + type(value).__name__)
                compare_result, sub_reasons = match_method(src_value[item], value)
                if not compare_result:
                    match = False
                    reasons.append(
                        "{0} not found in {1}".format(json.dumps(value), json.dumps(src_value[item]))
                    )
            else:
                raise OpenShiftException(
                    "compare_dict: Encountered unimplemented type {0}".format(type(value).__name__)
                )
        return match, reasons

    def compare_obj_list(self, src_value, request_value, obj_class):
        """
        Compare a type of object to a dict. Returns bool indicating if they match, and a list
        of strings describing why not.
        :param src_value: A sub-object from the existing API object.
        :param request_value: A dict from the request parameters.
        :return: match, reasons: boolean (whether or not they matched), list of strings
        """
        match = True
        sample_obj = getattr(client.models, obj_class)()
        reasons = []
        for item in request_value:
            if item is None:
                continue
            if not item.get('name'):
                raise OpenShiftException(
                    "Error: Expecting dict for {0} to contain a `name` attribute."
                )
            found = False
            for obj in src_value:
                if obj.name == item.get('name'):
                    # Assuming both the src_value and the request value include a name property
                    found = True
                    for key, value in item.items():
                        if type(value).__name__ in ('str', 'bool', 'int'):
                            if value != getattr(obj, key):
                                setattr(obj, key, value)
                                reasons.append(
                                    "In list {0}. Instance {1}, property {2} changed to {3}"
                                    .format(obj_class, obj.name, key, value)
                                )
                                match = False
                        elif type(value).__name__ == 'list':
                            if hasattr(sample_obj, 'swagger_types') and sample_obj.swagger_types.get(key):
                                # compare the requested list, which should be a list of dicts to a list of objects
                                obj_type = sample_obj.swagger_types.get(key).replace('list[', '').replace(']', '')
                                compare_result, sub_reasons =\
                                    self.compare_obj_list(getattr(obj, key), value, obj_type)
                            else:
                                # Straight list comparison
                                compare_result, sub_reasons = self.compare_list(getattr(obj, key), value)
                            if not compare_result:
                                reasons.append(
                                    "In list {0}. Instance {1}, property {2} changed to {3}"
                                    .format(obj_class, obj.name, key, str(value))
                                )
                                match = False
                        elif type(value).__name__ == 'dict':
                            compare_result, sub_reasons = self.compare_dict(getattr(obj, key), value)
                            if not compare_result:
                                reasons.append(
                                    "In list {0}. Instance {1}, property {2} changed to {3}"
                                    .format(obj_class, obj.name, key, str(value))
                                )
                                match = False
                        else:
                            raise OpenShiftException(
                                "compare_obj_list: In model {0} encountered unimplemented type {0}"
                                .format(self.get_base_model_name_snake(obj_class), type(value).__name__)
                            )
            if not found:
                # No matching name found. Add a new instance to the list.
                for key, value in item.items():
                    setattr(sample_obj, key, value)
                    src_value.append(sample_obj)
                    reasons.append(
                        "In list {0}. Added new instance for {1}."\
                        .format(obj_class, str(value))
                    )
                    match = False

        return match, reasons

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