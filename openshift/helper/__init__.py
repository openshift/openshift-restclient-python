# -*- coding: utf-8 -*-
from __future__ import absolute_import

import inspect
import re
import copy
import json
import logging

import string_utils

from logging import config as logging_config

from kubernetes import config
from kubernetes.config.config_exception import ConfigException
from kubernetes.client.rest import ApiException

from openshift import client
from openshift.client.models import V1DeleteOptions

# Regex for finding versions
VERSION_RX = re.compile("V\d((alpha|beta)\d)?")

BASE_API_VERSION = 'V1'

# Attributes in argspec not needed by Ansible
ARG_ATTRIBUTES_BLACKLIST = ('description', 'auth_option', 'property_path')


logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'KubeObjHelper.log',
            'mode': 'w',
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
    argspec_cache = None

    def __init__(self, api_version, kind, debug=False):
        self.api_version = api_version
        self.kind = kind
        self.model = self.get_model(api_version, kind)
        self.properties = self.properties_from_model_obj(self.model())
        self.base_model_name = self.model.__name__.replace(api_version.capitalize(), '')
        self.base_model_name_snake = string_utils.camel_case_to_snake(self.base_model_name)

        if debug:
            self.enable_debug()

    @staticmethod
    def enable_debug():
        """
        Turn on debugging, which will write to a file named 'KubeObjHelper.log'.

        NOTE: If you're running via an Ansible module, and targeting a remote node,
        the output will end up on the remote node, which is most likely not helpful.

        :return: None
        """
        LOGGING['loggers']['openshift.helper']['level'] = 'DEBUG'
        logging_config.dictConfig(LOGGING)

    def set_client_config(self, module_params):
        """
        Handles loading client config from a file, or updating the config object with any user provided
        authentication data.

        :param module_params: dict of params from AnsibleModule
        :param module_arg_spec: dict containing the Ansible module argument_spec
        :return: None
        """
        if module_params.get('kubeconfig') or module_params.get('context'):
            # Attempt to load config from file
            try:
                config.load_kube_config(config_file=module_params.get('kubeconfig'),
                                        context=module_params.get('context'))
            except IOError as e:
                raise OpenShiftException("Failed to access {}. Does the file exist?".format(
                    module_params.get('kubeconfig')), error=str(e))
            except ConfigException as e:
                raise OpenShiftException("Error accessing context {}.".format(
                    module_params.get('context')), error=str(e))
        elif module_params.get('api_url') or module_params.get('api_key') or module_params.get('username'):
            # Anything in argspec with an auth_option attribute, can be copied
            for arg_name, arg_value in self.argspec.items():
                if arg_value.get('auth_option'):
                    if module_params.get(arg_name, None) is not None:
                        setattr(client.configuration, arg_name, module_params[arg_name])
        else:
            # The user did not pass any options, so load the default kube config file, and use the active
            # context
            try:
                config.load_kube_config()
            except Exception as e:
                raise OpenShiftException("Error loading configuration: {}".format(str(e)))

    def get_object(self, name, namespace=None):
        k8s_obj = None
        try:
            get_method = self.__lookup_method('read', namespace)
            if namespace is None:
                k8s_obj = get_method(name)
            else:
                k8s_obj = get_method(name, namespace)
        except ApiException as exc:
            if exc.status != 404:
                msg = json.loads(exc.body).get('message', exc.reason)
                raise OpenShiftException(msg, status=exc.status)
        return k8s_obj

    def patch_object(self, name, namespace, k8s_obj):
        # TODO: add a parameter for waiting until the object is ready
        k8s_obj.status = None
        k8s_obj.metadata.resource_version = None
        try:
            patch_method = self.__lookup_method('patch', namespace)
            if namespace:
                return_obj = patch_method(name, namespace, k8s_obj)
            else:
                return_obj = patch_method(name, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason)
            raise OpenShiftException(msg, status=exc.status)
        return return_obj

    def create_object(self, namespace, k8s_obj):
        # TODO: add a parameter for waiting until the object is ready
        try:
            create_method = self.__lookup_method('create', namespace)
            if namespace is None:
                return_obj = create_method(k8s_obj)
            else:
                return_obj = create_method(namespace, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason)
            raise OpenShiftException(msg, status=exc.status)
        return return_obj

    def delete_object(self, name, namespace, delete_opts=None):
        # TODO: add a parameter for waiting until the object has been deleted
        # TODO: deleting a namespace requires a body
        delete_method = self.__lookup_method('delete', namespace)
        if not namespace:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    delete_method(name, body=V1DeleteOptions())
                else:
                    delete_method(name)
            except ApiException as exc:
                raise OpenShiftException(exc.reason, status=exc.status)
        else:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    delete_method(name, namespace, body=V1DeleteOptions())
                else:
                    delete_method(name, namespace)
            except ApiException as exc:
                msg = json.loads(exc.body).get('message', exc.reason)
                raise OpenShiftException(msg, status=exc.status)

    def update_object(self, name, namespace, k8s_obj):
        pass

    def object_from_params(self, module_params):
        """
        Instantiate an instance of the model class, and populate its attributes
        from the module parameters

        :param module_params: Dict of key:value pairs
        :return: The instantiated instance
        """
        self.__log_argspec()
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
            obj_prop = k8s_obj
            for prop in self.argspec[param_name]['property_path']:
                obj_prop = getattr(obj_prop, prop)
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
            elif type(obj_prop).__name__ in ('list', 'dict'):
                compare_method = getattr(self, 'compare_' + type(obj_prop).__name__)
                # perform comparison and update the object property
                compare_result, sub_reasons = compare_method(obj_prop, module_params[param_name])
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
        match = True
        reasons = []
        for item in request_value:
            if type(item).__name__ in ('str', 'int', 'bool') and item not in src_value:
                # type of request item is not a dict or list
                reasons.append(
                    "{0} from request list not found in {1}".format(item, json.dumps(src_value))
                )
                match = False
                src_value.append(item)
            elif type(item).__name__ in ('dict', 'list'):
                # type of request item is a dict or list
                match_method = getattr(self, '__compare_' + type(item).__name__)
                found_match = False
                for src_item in src_value:
                    compare_result, reason = match_method(src_item, item)
                    if compare_result:
                        found_match = True
                        break
                if not found_match:
                    reasons.append(
                        "{0} not found in {1}".format(json.dumps(item), json.dumps(src_value))
                    )
                    match = False
                    src_value.append(item)
            else:
                raise OpenShiftException(
                    "__compare_list: Encountered unimplemented object type {0}".format(type(item).__name__)
                )
        return match, reasons

    def compare_dict(self, src_value, request_value):
        match = True
        reasons = []
        for item, value in request_value:
            if not src_value.get(item):
                reasons.append(
                    "key {0} not found in {1}".format(item, json.dumps(src_value))
                )
                src_value[item] = value
                match = False
            if type(value).__name__ in ('str', 'int', 'bool') and value != src_value[item]:
                reasons.append(
                    "{0}: {1} not found in src dict {2}".format(item, value, json.dumps(src_value))
                )
                src_value[item] = value
                match = False
            elif type(value).__name__ in ('list', 'dict'):
                match_method = getattr(self, '__compare_' + type(value).__name__)
                compare_result, sub_reasons = match_method(src_value[item], value)
                if not compare_result:
                    match = False
                    reasons.append(
                        "{0} not found in {1}".format(json.dumps(value), json.dumps(src_value[item]))
                    )
            else:
                raise OpenShiftException(
                    "__compare_dict: Encountered unimplemented object type {0}".format(type(item).__name__)
                )
        return match, reasons

    @classmethod
    def properties_from_model_obj(cls, model_obj):
        """
        Introspect an object, and return a dict of 'name:dict of properties' pairs. The properties include: class,
        and immutable (a bool).

        :param model_obj: An object instantiated from openshift.client.models
        :return: dict
        """
        model_class = type(model_obj)

        # Create a list of model properties. Each property is represented as a dict of key:value pairs
        #  If a property does not have a setter, it's considered to be immutable
        properties = [
            {'name': x,
             'immutable': False if getattr(getattr(model_class, x), 'setter', None) else True
             }
            for x in dir(model_class) if isinstance(getattr(model_class, x), property)
        ]

        result = {}
        for prop in properties:
            prop_kind = model_obj.swagger_types[prop['name']]
            if prop_kind in ('str', 'int', 'bool'):
                prop_class = eval(prop_kind)
            elif prop_kind.startswith('list['):
                prop_class = list
            elif prop_kind.startswith('dict('):
                prop_class = dict
            else:
                prop_class = getattr(client.models, prop_kind)
            result[prop['name']] = {
                'class': prop_class,
                'immutable': prop['immutable']
            }
        return result

    def __lookup_method(self, operation, namespace=None):
        """
        Get the requested method (e.g. create, delete, patch, update) for
        the model object.
        :param operation: one of create, delete, patch, update
        :param namespace: optional name of the namespace.
        :return: pointer to the method
        """
        # TODO: raise error if method not found
        method_name = operation
        method_name += '_namespaced_' if namespace else '_'
        method_name += self.kind

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
    def get_model(api_version, kind):
        """
        Return the model class for the requested object.

        :param api_version: API version string
        :param kind: The name of object type (i.e. Service, Route, Container, etc.)
        :return: class
        """
        camel_kind = string_utils.snake_case_to_camel(kind)
        # capitalize the first letter of the string without lower-casing the remainder
        name = camel_kind[:1].capitalize() + camel_kind[1:]
        model_name = api_version.capitalize() + name
        try:
            model = getattr(client.models, model_name)
        except Exception as exc:
            raise OpenShiftException(
                    "Error: openshift.client.models.{} was not found. "
                    "Did you specify the correct Kind and API Version?".format(model_name)
            )
        return model

    @property
    def argspec(self):
        """
        Introspect the model properties, and return an Ansible module arg_spec dict.

        :return: dict
        """
        if self.argspec_cache:
            return self.argspec_cache

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

        if re.search(r'list$', self.base_model_name) and argument_spec.get('items'):
            # Lists are read only, so having a 'state' option doesn't make sense
            argument_spec.pop('state')

        self.argspec_cache = argument_spec
        self.__log_argspec()
        return self.argspec_cache

    def __log_argspec(self):
        """
        Safely logs the argspec by not including any params with the no_log attribute.

        :return: None
        """
        logger.debug("arg_spec:")
        tmp_arg_spec = copy.deepcopy(self.argspec)
        for key in tmp_arg_spec.keys():
            if tmp_arg_spec[key].get('no_log'):
                tmp_arg_spec.pop(key)
        logger.debug(json.dumps(tmp_arg_spec, indent=4, sort_keys=True))

    def __transform_properties(self, properties, prefix='', path=[], alternate_prefix=''):
        """
        Convert a list of properties to an argument_spec dictionary

        :param properties: List of properties from self.properties_from_model_obj()
        :param prefix: String to prefix to argument names.
        :param path: List of property names providing the recursive path through the model to the property
        :param alternate_prefix: a more minimal version of prefix
        :return: dict
        """
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
                        'property_path': ['metadata', 'labels']
                    }
                if 'annotations' in dir(prop_attributes['class']):
                    args['annotations'] = {
                        'type': 'dict',
                        'property_path': ['metadata', 'annotations']
                    }
                if 'namespace' in dir(prop_attributes['class']):
                    args['namespace'] = {
                        'property_path': ['metadata', 'namespace']
                    }
                if 'name' in dir(prop_attributes['class']):
                    args['name'] = {
                        'required': True,
                        'property_path': ['metadata', 'name']
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
