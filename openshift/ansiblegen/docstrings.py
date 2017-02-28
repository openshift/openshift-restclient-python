# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

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
        except OpenShiftException:
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

        if not self.helper.base_model_name_snake.endswith('_list'):
            # module allows CRUD operations on the object
            doc_string['description'] = [
                "Manage the lifecycle of a {} object. Supports check mode, and attempts to "
                "to be idempotent.".format(self.helper.base_model_name_snake)
            ]
        else:
            # module allows read only operations
            base_name = self.helper.base_model_name_snake.replace('_list', '')
            if not base_name.endswith('s'):
                base_name += 's'
            doc_string['description'] = [
                "Retrieve a list of {}. List operations provide a snapshot read of the "
                "underlying objects, returning a resource_version representing a consistent "
                "version of the listed objects.".format(base_name)
            ]
        doc_string['version_added'] = ANSIBLE_VERSION_ADDED
        doc_string['author'] = "OpenShift (@openshift)"
        doc_string['options'] = CommentedMap()
        doc_string['requirements'] = ["openshift == {}".format(openshift_version)]

        def add_option(pname, pdict, descr=None):
            """
            Adds a new parameter option to doc_string['options'].
            :param pname: name of the option
            :param pdict: dict of option attributes
            :param descr: option list of description strings
            :return: None
            """
            doc_string['options'][pname] = CommentedMap()
            if descr:
                doc_string['options'][pname]['description'] = descr
            elif pdict.get('description'):
                doc_string['options'][pname]['description'] = pdict['description']
            if pdict.get('required'):
                doc_string['options'][pname]['required'] = True
            if pdict.get('default', None) is not None:
                doc_string['options'][pname]['default'] = pdict['default']
            if pdict.get('choices'):
                doc_string['options'][pname]['choices'] = pdict['choices']
            if pdict.get('aliases'):
                doc_string['options'][pname]['aliases'] = pdict['aliases']

        for param_name in sorted(self.helper.argspec.keys()):
            param_dict = self.helper.argspec[param_name]
            if param_dict.get('property_path'):
                # parameter comes from the model
                obj = self.helper.model()
                for path in param_dict['property_path']:
                    kind = obj.swagger_types[path]
                    if kind in ('str', 'bool', 'int') or \
                       kind.startswith('dict(') or \
                       kind.startswith('list['):
                        docs = inspect.getdoc(getattr(type(obj), path))
                        string_list = self.__doc_clean_up(docs.split('\n'))
                        add_option(param_name, param_dict, descr=string_list)
                    else:
                        obj = getattr(models, kind)()
            elif param_dict.get('description'):
                # parameters is hard-coded in openshift.helper
                add_option(param_name, param_dict)

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
        obj_name = self.helper.base_model_name_snake
        doc_string[obj_name] = CommentedMap()
        doc_string[obj_name]['type'] = 'complex'
        doc_string[obj_name]['returned'] = 'when I(state) = C(present)'
        doc_string[obj_name]['contains'] = CommentedMap()
        obj = self.helper.model()
        self.__get_attributes(obj, doc_key=doc_string[obj_name]['contains'])
        return ruamel.yaml.dump(doc_string, Dumper=ruamel.yaml.RoundTripDumper)

    def __get_attributes(self, obj, doc_key=None):
        """
        Recursively inspect the attributes of a given obj

        :param obj: model object
        :param doc_key: pointer to the current position in doc_string dict
        :return: None
        """
        model_class = type(obj)
        for attribute in dir(model_class):
            if isinstance(getattr(model_class, attribute), property):
                kind = obj.swagger_types[attribute]
                docs = inspect.getdoc(getattr(type(obj), attribute))
                string_list = self.__doc_clean_up(docs.split('\n'))
                if kind in ('str', 'int', 'bool'):
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = kind
                elif kind.startswith('list['):
                    class_name = kind.replace('list[', '').replace(']', '')
                    logger.debug(class_name)
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = 'list'
                    sub_obj = None
                    try:
                        sub_obj = getattr(models, class_name)()
                    except Exception:
                        pass
                    if sub_obj:
                        doc_key[attribute]['contains'] = CommentedMap()
                        self.__get_attributes(sub_obj, doc_key=doc_key[attribute]['contains'])
                    else:
                        doc_key[attribute]['contains'] = class_name
                elif kind.startswith('dict('):
                    logger.debug(kind)
                    class_name = kind.replace('dict(', '').replace(')', '')
                    logger.debug(class_name)
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = 'complex'
                    sub_obj = None
                    try:
                        sub_obj = getattr(models, class_name)()
                    except Exception:
                        pass
                    if sub_obj:
                        doc_key[attribute]['contains'] = CommentedMap()
                        self.__get_attributes(sub_obj, doc_key=doc_key[attribute]['contains'])
                    else:
                        doc_key[attribute]['contains'] = class_name
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
