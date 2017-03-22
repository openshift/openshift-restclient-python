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

from dictdiffer import diff

from kubernetes import watch
from kubernetes.client.rest import ApiException
from kubernetes.config.config_exception import ConfigException

from openshift import client, config
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
    def __init__(self, api_version, kind, debug=False, reset_logfile=True, timeout=20, **auth):
        self.api_version = api_version
        self.kind = kind
        self.model = self.get_model(api_version, kind)
        self.properties = self.properties_from_model_obj(self.model())
        self.base_model_name = self.get_base_model_name(self.model.__name__)
        self.base_model_name_snake = self.get_base_model_name_snake(self.base_model_name)
        self.timeout = timeout  # number of seconds to wait for an API request
        self.is_openshift = False

        if debug:
            self.enable_debug(reset_logfile)

        self.set_client_config(**auth)

    def set_client_config(self, **auth):
        """ Convenience method for updating the configuration object, and instantiating a new client """
        config_file = auth.get('kubeconfig')
        context = auth.get('context')

        try:
            self.api_client = config.new_client_from_config(config_file, context)
        except ConfigException as e:
            raise OpenShiftException(
                "Error accessing context {}.".format(auth.get('context')), error=str(e))
        except IOError as e:
            if config_file is not None:
                # Missing specified config file, cannot continue
                raise OpenShiftException(
                    "Failed to access {}. Does the file exist?".format(config_file), error=str(e)
                )
            else:
                # Default config is missing, but other auth params may be provided, continue
                logger.debug("Unable to load default config: {}".format(e))

        if auth.get('host') is not None:
            self.api_client.host = auth['host']

        auth_keys = ['api_key', 'ssl_ca_cert', 'cert_file', 'key_file', 'verify_ssl']

        for key in auth_keys:
            if auth.get(key, None) is not None:
                if key == 'api_key':
                    self.api_client.config.api_key = {'authorization': auth[key]}
                else:
                    setattr(self.api_client.config, key, auth[key])

        try:
            client.OapiApi(api_client=self.api_client).get_api_resources()
            self.is_openshift = True
        except (ApiException,MaxRetryError):
            pass

    @staticmethod
    def enable_debug(reset_logfile=True):
        """ Turn on debugging. If reset_logfile, then remove the existing log file. """
        if reset_logfile:
            LOGGING['handlers']['file']['mode'] = 'w'
        LOGGING['loggers'][__name__]['level'] = 'DEBUG'
        logging_config.dictConfig(LOGGING)

    def get_object(self, name, namespace=None):
        k8s_obj = None
        method_name = 'list' if self.kind.endswith('list') else 'read'
        try:
            get_method = self.lookup_method(method_name, namespace)
            if name and namespace is None:
                k8s_obj = get_method(name)
            elif namespace and not name:
                k8s_obj = get_method(namespace)
            else:
                k8s_obj = get_method(name, namespace)
        except ApiException as exc:
            if exc.status != 404:
                if self.base_model_name == 'Project' and exc.status == 403:
                    pass
                else:
                    msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
                    raise OpenShiftException(msg, status=exc.status)
        return k8s_obj

    def patch_object(self, name, namespace, k8s_obj):
        logger.debug('Starting patch object')
        empty_status = self.properties['status']['class']()
        k8s_obj.status = empty_status
        k8s_obj.metadata.resource_version = None
        self.__remove_creation_timestamps(k8s_obj)
        w, stream = self.__create_stream(namespace)
        logger.debug("Patching object: {}".format(json.dumps(k8s_obj.to_dict())))
        try:
            patch_method = self.lookup_method('patch', namespace)
            if namespace:
                patch_method(name, namespace, k8s_obj)
            else:
                patch_method(name, k8s_obj)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
            raise OpenShiftException(msg, status=exc.status)
        except MaxRetryError as ex:
            raise OpenShiftException(str(ex.reason))

        return_obj = self.__read_stream(w, stream, name, 'patch')
        if not return_obj:
            return_obj = self.__wait_for_response(name, namespace, 'patch')
        return return_obj

    def create_project(self, metadata, display_name=None, description=None):
        """ Creating a project requires using the project_request endpoint. Because, why
            on earth would you follow the same pattern as every other object? Instead, we
            created a special snowflake. Yay!!!

            Also, just to be extra special, creating a project does not generate events.
        """
        # TODO: handle admin-level project creation

        w, stream = self.__create_stream(None)
        try:
            proj_req = client.V1ProjectRequest(metadata=metadata, display_name=display_name, description=description)
            client.OapiApi(self.api_client).create_project_request(proj_req)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
            raise OpenShiftException(msg, status=exc.status)

        return_obj = self.__read_stream(w, stream, metadata.name, 'create')
        if not return_obj:
            return_obj = self.__wait_for_response(metadata.name, None, 'create')

        return return_obj

    def create_object(self, namespace, k8s_obj=None, body=None):
        """
        Send a POST request to the API. Pass either k8s_obj or body.
        :param namespace: namespace value or None
        :param k8s_obj: optional k8s object model
        :param body: optional JSON dict
        :return: new object returned from the API
        """
        logger.debug('Starting create object')
        w, stream = self.__create_stream(namespace)
        name = None
        if k8s_obj:
            name = k8s_obj.metadata.name
        elif body:
            name = body.get('metadata', {}).get('name', None)
        try:
            create_method = self.lookup_method('create', namespace)
            if namespace:
                if k8s_obj:
                    create_method(namespace, k8s_obj)
                else:
                    create_method(namespace, body=body)
            else:
                if k8s_obj:
                    create_method(k8s_obj)
                else:
                    create_method(body=body)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
            raise OpenShiftException(msg, status=exc.status)

        return_obj = self.__read_stream(w, stream, name, 'create')

        if not return_obj:
            return_obj = self.__wait_for_response(name, namespace, 'create')

        return return_obj

    def delete_object(self, name, namespace):
        logger.debug('Starting delete object {0} {1} {2}'.format(self.kind, name, namespace))
        delete_method = self.lookup_method('delete', namespace)

        if self.kind in ('project', 'namespace'):
            w, stream = self.__create_stream(namespace)

        status_obj = None
        if not namespace:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    status_obj = delete_method(name, body=V1DeleteOptions())
                else:
                    status_obj = delete_method(name)
            except ApiException as exc:
                msg = json.loads(exc.body).get('message', exc.reason)
                raise OpenShiftException(msg, status=exc.status)
        else:
            try:
                if 'body' in inspect.getargspec(delete_method).args:
                    status_obj = delete_method(name, namespace, body=V1DeleteOptions())
                else:
                    status_obj = delete_method(name, namespace)
            except ApiException as exc:
                msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
                raise OpenShiftException(msg, status=exc.status)

        if status_obj is None or status_obj.status == 'Failure':
            msg = 'Failed to delete {}'.format(name)
            if namespace is not None:
                msg += ' in namespace {}'.format(namespace)
            msg += ' status: {}'.format(status_obj)
            raise OpenShiftException(msg)

        self.__wait_for_response(name, namespace, 'delete')

    def replace_object(self, name, namespace, k8s_obj=None, body=None):
        """ Replace an existing object. Pass in a model object or request dict().
            Will first lookup the existing object to get the resource version and
            update the request.
        """
        logger.debug('Starting replace object')
        existing_obj = self.get_object(name, namespace)
        if not existing_obj:
            msg = "Error: Replacing object. Unable to find {}".format(name)
            msg += " in namespace {}".format(namespace) if namespace else ""
            raise OpenShiftException(msg)
        if k8s_obj:
            k8s_obj.status = self.properties['status']['class']()
            self.__remove_creation_timestamps(k8s_obj)
            k8s_obj.metadata.resource_version = existing_obj.metadata.resource_version
        elif body:
            body['metadata']['resourceVersion'] = existing_obj.metadata.resource_version
        w, stream = self.__create_stream(namespace)
        try:
            replace_method = self.lookup_method('replace', namespace)
            if k8s_obj:
                if namespace is None:
                    replace_method(name, k8s_obj)
                else:
                    replace_method(name, namespace, k8s_obj)
            else:
                if namespace is None:
                    replace_method(name, body=body)
                else:
                    replace_method(name, namespace, body=body)
        except ApiException as exc:
            msg = json.loads(exc.body).get('message', exc.reason) if exc.body.startswith('{') else exc.body
            raise OpenShiftException(msg, status=exc.status)

        return_obj = self.__read_stream(w, stream, name, 'replace')
        if not return_obj:
            return_obj = self.__wait_for_response(name, namespace, 'replace')

        return return_obj

    @staticmethod
    def objects_match(obj_a, obj_b):
        """ Test the equality of two objects. Returns bool, list(differences). """
        match = False
        diffs = []
        if obj_a is None and obj_b is None:
            match = True 
        elif not obj_a or not obj_b:
            pass  
        elif type(obj_a).__name__ != type(obj_b).__name__:
            pass 
        else:
            dict_a = obj_a.to_dict()
            dict_b = obj_b.to_dict()
            diffs = list(diff(dict_a, dict_b))
            match = len(diffs) == 0
        return match, diffs

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
        method_name += self.kind.replace('_list', '') if self.kind.endswith('_list') else self.kind

        apis = [x for x in dir(client.apis) if VERSION_RX.search(x)]
        apis.append('OapiApi')

        method = None
        for api in apis:
            api_class = getattr(client.apis, api)
            method = getattr(api_class(self.api_client), method_name, None)
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
    def attribute_to_snake(name):
        """ Convert an object property name from camel to snake """
        result = string_utils.camel_case_to_snake(name)
        if result.endswith('_i_p'):        
           result = re.sub(r'\_i\_p$', '_ip', result) 
        return result
 
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
        w._api_client = self.api_client  # monkey patch for access to OpenShift models
        list_method = self.lookup_method('list', namespace)
        if namespace:
            stream = w.stream(list_method, namespace, _request_timeout=self.timeout)
        else:
            stream = w.stream(list_method, _request_timeout=self.timeout)
        return w, stream

    def __read_stream(self, watcher, stream, name, action):
        # TODO https://cobe.io/blog/posts/kubernetes-watch-python/    <--- might help?

        return_obj = None

        try:
            for event in stream:
                if action == 'delete':
                    event_types = ['DELETED']
                else:
                    event_types = ['ADDED', 'MODIFIED']

                if event['object'].metadata.name == name:
                    obj = None
                    if event.get('object'):
                        obj_json = json.dumps(event['object'].to_dict())
                        logger.debug(
                            "EVENT type: {0} object: {1}".format(event['type'], obj_json)
                        )
                        obj = event['object']
                    else:
                        logger.debug(repr(event))

                    if event['type'] in event_types:
                        if event['type'] == 'DELETED':
                           # Object was deleted
                            return_obj = obj
                            watcher.stop()
                            break
                        else:
                            # TODO: better handle modified events to ensure we are returning the right one
                            # Object is either added or modified. Check the status and determine if we
                            #  should continue waiting
                            status = getattr(obj, 'status', None)

                            # if self.kind == 'namespace':
                            #     if self.is_openshift:
                            #         try:
                            #             annotation_keys = obj.metadata.annotations.keys()
                            #             required_annotations = [u'openshift.io/sa.scc.mcs',
                            #                                     u'openshift.io/sa.scc.supplemental-groups',
                            #                                     u'openshift.io/sa.scc.uid-range']
                            #             for key in required_annotations:
                            #                 if key not in annotation_keys:
                            #                     continue
                            #         except AttributeError:
                            #             continue
                            #     if status.phase == 'Active':
                            #         return_obj = obj
                            #         watcher.stop()
                            #         break
                            if self.kind == 'route':
                                route_statuses = set()
                                for route_ingress in status.ingress:
                                    for condition in route_ingress.conditions:
                                        route_statuses.add(condition.type)
                                if route_statuses <= set(['Ready', 'Admitted']):
                                    return_obj = obj
                                    watcher.stop()
                                    break
                            elif self.kind in ['service', 'deployment_config']:
                                return_obj = obj
                                watcher.stop()
                                break
                            else:
                                if hasattr(status, 'phase'):
                                    if status.phase == 'Active':
                                        # TODO other phase values ??
                                        # TODO test namespaces for OpenShift annotations if needed
                                        return_obj = obj
                                        watcher.stop()
                                        break
                                elif hasattr(status, 'conditions'):
                                    # TODO: attempt to handle generic conditions better
                                    conditions = getattr(status, 'conditions')
                                    if conditions and len(conditions) > 0:
                                        # We know there is a status, but it's up to the user to determine meaning.
                                        return_obj = obj
                                        watcher.stop()
                                        break
        except Exception as exc:
            # A timeout occurred
            logger.debug('STREAM FAILED: {}'.format(exc))
            pass

        return return_obj
