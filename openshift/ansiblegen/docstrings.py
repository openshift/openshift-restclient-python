# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import  print_function

from collections import OrderedDict

import logging
import inspect
import string_utils
import re

import ruamel.yaml
from ruamel.yaml.comments import CommentedMap

from openshift import __version__ as openshift_version
from openshift.client import models
from openshift.helper import KubernetesObjectHelper, OpenShiftException

logger = logging.getLogger(__name__)

# Once the modules land in Ansible core, this should not change
ANSIBLE_VERSION_ADDED = "2.3.0"


class DocStrings(object):

    def __init__(self, model, api_version):
        self.model = model
        self.api_version = api_version
        try:
            self.helper = KubernetesObjectHelper(self.api_version, self.model)
        except OpenShiftException as exc:
            raise

    @property
    def documentation(self):
        """
        Generate the DOCUMENTATION string for use in an Ansible module.

        :return: string containing formatted YAML
        """
        doc_string = CommentedMap()   # Gives us an OrderedDict that ruamel.yaml supports
        doc_string['module'] = "k8s_{0}_{1}".format(self.api_version.lower(),
                                                    string_utils.camel_case_to_snake(self.model))
        doc_string['short_description'] = "Kubernetes {}".format(self.helper.base_model_name)
        doc_string['description'] = [
            "Manage the lifecycle of a {} object. Supports check mode, and attempts to " \
            "to be idempotent.".format(self.helper.base_model_name)
        ]
        doc_string['version_added'] = ANSIBLE_VERSION_ADDED
        doc_string['author'] = "OpenShift (@openshift)"
        doc_string['options'] = CommentedMap()
        doc_string['requirements'] = ["openshift == {}".format(openshift_version)]

        for param_name in sorted(self.helper.argspec.keys()):
            param_dict = self.helper.argspec[param_name]
            if param_dict.get('property_path'):
                obj = self.helper.model()
                for path in param_dict['property_path']:
                    kind = obj.swagger_types[path]
                    if kind in ('str', 'bool', 'int') or \
                       kind.startswith('dict(') or kind.startswith('list['):
                        docs = inspect.getdoc(getattr(type(obj), path))
                        string_list = self.__doc_clean_up(docs.split('\n'))
                        doc_string['options'][param_name] = {
                            'description': string_list
                        }
                        if param_dict.get('required'):
                            doc_string['options'][param_name]['required'] = True
                        if param_dict.get('default', None) is not None:
                            doc_string['options'][param_name]['default'] = param_dict['default']
                    else:
                        obj = getattr(models, kind)()
        return ruamel.yaml.dump(doc_string, Dumper=ruamel.yaml.RoundTripDumper)

    @property
    def return_block(self):
        """
        Generate the RETURN doc string for use in an Ansible module.

        :return: string containing formatted YAML
        """
        doc_string = CommentedMap()
        doc_string['api_version'] = {
            'type': 'string',
            'description': 'Requested API version',
        }
        doc_string['kind'] = CommentedMap()
        doc_string['kind']['type'] = 'complex'
        doc_string['kind']['returned'] = 'when I(state) = C(present)'
        doc_string['kind']['contains'] = CommentedMap()
        obj = self.helper.model()
        self.__get_attributes(obj, doc_key=doc_string['kind'])
        return ruamel.yaml.dump(doc_string, Dumper=ruamel.yaml.RoundTripDumper)

    def __get_attributes(self, obj, doc_key=None):
        """
        Recursively inspect the attributes of a given obj

        :param obj: model object
        :param doc_key: pointer to the current position in doc_string dict
        :return: None
        """
        model_class = type(obj)
        logger.debug("model_class: {}".format(model_class))
        for attribute in dir(model_class):
            logger.debug("attribute: {}".format(attribute))
            if isinstance(getattr(model_class, attribute), property):
                logger.debug("is property")
                kind = obj.swagger_types[attribute]
                docs = inspect.getdoc(getattr(type(obj), attribute))
                string_list = self.__doc_clean_up(docs.split('\n'))
                if kind in ('str', 'int', 'bool') or \
                   kind.startswith('list[') or \
                   kind.startswith('dict('):
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = kind
                else:
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = 'complex'
                    doc_key[attribute]['contains'] = CommentedMap()
                    sub_obj = getattr(models, kind)()
                    self.__get_attributes(sub_obj, doc_key=doc_key[attribute]['contains'])

    @staticmethod
    def __doc_clean_up(doc_strings):
        result = []
        for line in doc_strings:
            if re.match(':', line):
                continue
            if line == '':
                continue
            if re.match('Gets the', line) or re.match('Sets the', line):
                continue
            result.append(line)
        return result
