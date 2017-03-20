# -*- coding: utf-8 -*-
from __future__ import absolute_import

import inspect
import json
import logging
import math
import re
import time

import string_utils

from logging import config as logging_config

from kubernetes import config, watch
from kubernetes.client.rest import ApiException
from kubernetes.config.config_exception import ConfigException

from openshift import client
from openshift.client import configuration, ApiClient
from openshift.client.models import V1DeleteOptions

from .exceptions import OpenShiftException

# Regex for finding versions
VERSION_RX = re.compile("V\d((alpha|beta)\d)?")

BASE_API_VERSION = 'V1'

logger = logging.getLogger(__name__)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'KubeObjHelper.log',
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


class KubernetesObjectHelper(object):

    def __init__(self, api_version, kind, debug=False, reset_logfile=True, timeout=60):
        self.api_version = api_version
        self.kind = kind
        self.model = self.get_model(api_version, kind)
        self.properties = self.properties_from_model_obj(self.model())
        self.base_model_name = self.get_base_model_name(self.model.__name__)
        self.base_model_name_snake = self.get_base_model_name_snake(self.base_model_name)
        self.timeout = timeout  # number of seconds to wait for an API request

        if debug:
            self.enable_debug(reset_logfile)

        try:
            config.load_kube_config()
        except Exception as exc:
            logger.debug("Unable to load default config: {}".format(exc))

        self.api_client = self.api_client = ApiClient()

    def set_client_config(self, **kwargs):
        """ Convenience method for updating the configuration object, and instantiating a new client """
        if kwargs.get('kubeconfig') or kwargs.get('context'):
            # Attempt to load config from file
            try:
                config.load_kube_config(config_file=kwargs.get('kubeconfig'),
                                        context=kwargs.get('context'))
            except IOError as e:
                raise OpenShiftException(
                    "Failed to access {}. Does the file exist?".format(kwargs.get('kubeconfig')), error=str(e)
                )
            except ConfigException as e:
                raise OpenShiftException(
                    "Error accessing context {}.".format(kwargs.get('context')), error=str(e))

        auth_keys = ['api_key', 'host', 'ssl_ca_cert', 'cert_file', 'key_file', 'verify_ssl']
        for key in auth_keys:
            if kwargs.get(key, None) is not None:
                if key == 'api_key':
                    configuration.api_key = {'authorization': kwargs[key]}
                else:
                    setattr(configuration, key, kwargs[key])
        self.api_client = self.api_client = ApiClient()

    @staticmethod
    def enable_debug(reset_logfile=True):
        """ Turn on debugging. If reset_logfile, then remove the existing log file. """
        if reset_logfile:
            LOGGING['handlers']['file']['mode'] = 'w'
        LOGGING['loggers'][__name__]['level'] = 'DEBUG'
        logging_config.dictConfig(LOGGING)

    def get_object(self, name, namespace=None):
        k8s_obj = None
        try:
            get_method = self.lookup_method('read', namespace)
            if namespace is None:
                k8s_obj = get_method(name)
            else:
                k8s_obj = get_method(name, namespace)
        except ApiException as ex:
            if ex.status != 404:
                if self.base_model_name == 'Project'and ex.status == 403:
                    pass
                else:
                    if ex.body:
                        msg = json.loads(ex.body).get('message', ex.reason)
                    else:
                        msg = str(ex)
                    raise OpenShiftException(msg, status=ex.status)
        return k8s_obj

    def patch_object(self, name, namespace, k8s_obj, wait=False, timeout=60):
        empty_status = self.properties['status']['class']()
        k8s_obj.status = empty_status
        k8s_obj.metadata.resource_version = None
        self.__remove_creation_timestamps(k8s_obj)
        #w, stream = self.__create_stream(namespace)
        logger.debug("Patching object: {}".format(json.dumps(k8s_obj.to_dict(), indent=4)))
        try:
            patch_method = self.lookup_method('patch', namespace)
            if namespace:
                return_obj = patch_method(name, namespace, k8s_obj)
            else:
                return_obj = patch_method(name, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason)
            raise OpenShiftException(msg, status=exc.status)
        #return_obj = self.__read_stream(w, stream, 'patch', name, namespace)
        return_obj = self.__wait_for_response(name, namespace, 'patch')
        return return_obj

    def create_project(self, metadata, display_name=None, description=None):
        # TODO: handle admin-level project creation
        try:
            proj_req = client.V1ProjectRequest(metadata=metadata, display_name=display_name, description=description)
            client.OapiApi().create_project_request(proj_req)
        except ApiException as ex:
            msg = json.loads(ex.body).get('message', ex.reason)
            raise OpenShiftException(msg, status=ex.status)

        return_obj = self.__wait_for_response(metadata.name, None, 'create')

        return return_obj

    def create_object(self, namespace, k8s_obj):
        #w, stream = self.__create_stream(namespace)
        try:
            create_method = self.lookup_method('create', namespace)
            if namespace is None:
                create_method(k8s_obj)
            else:
                create_method(namespace, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason)
            raise OpenShiftException(msg, status=exc.status)
        #return_obj = self.__read_stream(w, stream, 'create', k8s_obj.metadata.name, namespace)
        return_obj = self.__wait_for_response(k8s_obj.metadata.name, namespace, 'create')
        return return_obj

    def delete_object(self, name, namespace):
        delete_method = self.lookup_method('delete', namespace)
        #w, stream = self.__create_stream(namespace)
        if not namespace:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    delete_method(name, body=V1DeleteOptions())
                else:
                    delete_method(name)
            except ApiException as exc:
                msg = json.loads(exc.body).get('message', exc.reason)
                raise OpenShiftException(msg, status=exc.status)
        else:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    delete_method(name, namespace, body=V1DeleteOptions())
                else:
                    delete_method(name, namespace)
            except ApiException as exc:
                msg = json.loads(exc.body).get('message', exc.reason)
                raise OpenShiftException(msg, status=exc.status)
        #self.__read_stream(w, stream, 'delete', name, namespace)
        self.__wait_for_response(name, namespace, 'delete')

    def replace_object(self, name, namespace, k8s_obj):
        empty_status = self.properties['status']['class']()
        k8s_obj.status = empty_status
        k8s_obj.metadata.resource_version = None
        self.__remove_creation_timestamps(k8s_obj)
        #w, stream = self.__create_stream(namespace)
        try:
            replace_method = self.lookup_method('replace', namespace)
            if namespace is None:
                return_obj = replace_method(name, k8s_obj)
            else:
                return_obj = replace_method(name, namespace, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason)
            raise OpenShiftException(msg, status=exc.status)
        #retur_obj = self.__read_stream(w, stream, 'replace', name, namespace)
        return_obj = self.__wait_for_response(name, namespace, 'replace')
        return return_obj

    def objects_match(self, obj_a, obj_b):
        """ Test the equality of two objects. """
        if obj_a is None and obj_b is None:
            return True
        if not obj_a or not obj_b:
            return False
        if type(obj_a).__name__ != type(obj_b).__name__:
            return False
        return obj_a == obj_b

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

    def lookup_method(self, operation, namespace=None):
        """
        Get the requested method (e.g. create, delete, patch, update) for
        the model object.
        :param operation: one of create, delete, patch, update
        :param namespace: optional name of the namespace.
        :return: pointer to the method
        """

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
        if method is None:
            msg = "Did you forget to include the namespace?" if not namespace else ""
            raise OpenShiftException(
                "Error: method {0} not found for model {1}. {2}".format(method_name, self.kind, msg)
            )
        return method

    @staticmethod
    def get_base_model_name(model_name):
        """
        Return model_name with API Version removed.
        :param model_name: string
        :return: string
        """
        return VERSION_RX.sub('', model_name)

    def get_base_model_name_snake(self, model_name):
        """
        Return base model name with API version removed, and remainder converted to snake case
        :param model_name: string
        :return: string
        """
        result = self.get_base_model_name(model_name)
        return string_utils.camel_case_to_snake(result)

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
        except Exception:
            raise OpenShiftException(
                    "Error: openshift.client.models.{} was not found. "
                    "Did you specify the correct Kind and API Version?".format(model_name)
            )
        return model

    def __remove_creation_timestamps(self, obj):
        """ Recursively look for creation_timestamp property, and set it to None """
        if hasattr(obj, 'swagger_types'):
            for key, value in obj.swagger_types.items():
                if key == 'creation_timestamp':
                    obj.creation_timestamp = None
                    continue
                if value.startswith('dict(') or value.startswith('list['):
                    continue
                if value in ('str', 'int', 'bool'):
                    continue
                if getattr(obj, key) is not None:
                    self.__remove_creation_timestamps(getattr(obj, key))

    def __wait_for_response(self, name, namespace, action):
        """ Wait for an API response """
        tries = 0
        half = math.ceil(self.timeout / 2)
        obj = None
        while tries <= half:
            obj = self.get_object(name, namespace)
            if action == 'delete':
                if not obj:
                    break
            elif obj and obj.status and hasattr(obj.status, 'phase'):
                if obj.status.phase == 'Active':
                    break
            elif obj and obj.status:
                break
            tries += 2
            time.sleep(2)
        return obj

    def __create_stream(self, namespace):
        """ Create a stream that gets events for the our model """
        w = watch.Watch()
        w._api_client = self.api_client # monkey patch for access to OpenShift models
        list_method = self.lookup_method('list', namespace)
        if namespace:
            stream = w.stream(list_method, namespace, _request_timeout=self.timeout)
        else:
            stream = w.stream(list_method, _request_timeout=self.timeout)
        return w, stream

    def __read_stream(self, watcher, stream, action, name, namespace):
        #TODO https://cobe.io/blog/posts/kubernetes-watch-python/    <--- might help?
        return_obj = None
        try:
            for event in stream:
                logger.debug(
                    "EVENT type: {0} object: {1} {2} requested action: {3}".format(event['type'],
                                                                                   event['object'].kind,
                                                                                   event['object'].metadata.name,
                                                                                   action)
                )

                #TODO: Are these the correct event['type'] names?

                if action == 'create' and event['type'] == 'ADDED':
                    return_obj = event['object']
                elif action == 'delete' and event['type'] == 'DELETED':
                    return_obj = None
                    watcher.stop()
                    break
                elif action in ('patch', 'replace') and event['type'] == 'MODIFIED':
                    return_obj = event['object']

                if return_obj and return_obj.metadata.name == name and return_obj.metadata.namespace == namespace:
                    if return_obj.status and hasattr(return_obj.status, 'phase'):
                        if return_obj.status.phase == 'active':
                            watcher.stop()
                            break
                    elif return_obj.status:
                        watcher.stop()
                        break
        except Exception as exc:
            # A timeout occurred
            logger.debug('STREAM FAILED: {}'.format(exc))
            pass

        if action != 'delete' and return_obj is None:
            # Somehow we didn't get an event that matched our object
            return_obj = self.get_object(name, namespace)

        return return_obj
