# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import inspect
import logging
import os
import re
import string_utils
import shlex

import ruamel.yaml
from ruamel.yaml.comments import CommentedMap

from openshift import __version__ as openshift_version
from openshift.client import models
from openshift.helper import OpenShiftException
from openshift.helper.ansible import AnsibleModuleHelper

logger = logging.getLogger(__name__)


# Once the modules land in Ansible core, this should not change
ANSIBLE_VERSION_ADDED = "2.3.0"


class DocStrings(object):

    def __init__(self, model, api_version):
        self.model = model
        self.api_version = api_version
        try:
            self.helper = AnsibleModuleHelper(self.api_version, self.model)
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
                if isinstance(pdict.get('choices'), dict):
                    doc_string['options'][pname]['choices'] = [value for key, value in pdict['choices'].items()]
                else:
                    doc_string['options'][pname]['choices'] = pdict['choices']
            if pdict.get('aliases'):
                doc_string['options'][pname]['aliases'] = pdict['aliases']
            if pdict.get('type') and pdict.get('type') != 'str':
                doc_string['options'][pname]['type'] = pdict['type']

        for param_name in sorted([x for x, _ in self.helper.argspec.items()]):
            param_dict = self.helper.argspec[param_name]
            if param_name.endswith('params'):
                descr = [self.__params_descr(param_name)]
                add_option(param_name, param_dict, descr=descr)
            elif param_dict.get('property_path'):
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

        return ruamel.yaml.dump(doc_string, Dumper=ruamel.yaml.RoundTripDumper, width=80)

    def __params_descr(self, name):
        descr = None
        for arg in self.helper.argspec:
            if self.helper.argspec[arg].get('choices'):
                for key in self.helper.argspec[arg]['choices']:
                    if key in name:
                        descr = "When C({0}) is I({1}), provide a mapping of 'key:value' settings.".format(
                            arg, self.helper.argspec[arg]['choices'][key])
                        break
                if descr:
                    break
        return descr

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
        if self.helper.argspec.get('state'):
            doc_string[obj_name]['returned'] = 'when I(state) = C(present)'
        else:
            doc_string[obj_name]['returned'] = 'on success'
        doc_string[obj_name]['contains'] = CommentedMap()
        obj = self.helper.model()
        self.__get_attributes(obj, doc_key=doc_string[obj_name]['contains'])
        return ruamel.yaml.dump(doc_string, Dumper=ruamel.yaml.RoundTripDumper, width=80)

    def __get_attributes(self, obj, doc_key=None):
        """
        Recursively inspect the attributes of a given obj

        :param obj: model object
        :param doc_key: pointer to the current position in doc_string dict
        :return: None
        """
        model_class = type(obj)
        model_name = self.helper.get_base_model_name_snake(model_class.__name__)
        for attribute in dir(model_class):
            if isinstance(getattr(model_class, attribute), property):
                kind = obj.swagger_types[attribute]
                docs = inspect.getdoc(getattr(type(obj), attribute))
                string_list = self.__doc_clean_up(docs.split('\n'))
                if kind in ('str', 'int', 'bool'):
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = kind
                elif attribute.endswith('params'):
                    # Parameters are associate with a 'type' property. If the object has a 'type', then
                    #  it will also contain one or more 'param' objects, where each describes its
                    #  associated type. Rather than list every property of each param object, the
                    #  following attempts to summarize.
                    snake_name = string_utils.snake_case_to_camel(attribute.replace('_params', ''))
                    cap_snake_name = snake_name[:1].capitalize() + snake_name[1:]
                    model_name_text = ' '.join(model_name.split('_')).capitalize()
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = (
                        model_name_text + ' parameters when I(type) is {}.'.format(cap_snake_name)
                    )
                    doc_key[attribute]['type'] = 'complex'
                    doc_key[attribute]['returned'] = 'when I(type) is {}'.format(cap_snake_name)
                elif kind.startswith('list['):
                    class_name = kind.replace('list[', '').replace(']', '')
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = 'list'
                    sub_obj = None
                    try:
                        sub_obj = getattr(models, class_name)()
                    except:
                        pass
                    if sub_obj:
                        doc_key[attribute]['contains'] = CommentedMap()
                        self.__get_attributes(sub_obj, doc_key=doc_key[attribute]['contains'])
                    else:
                        doc_key[attribute]['contains'] = class_name
                elif kind.startswith('dict('):
                    class_name = kind.replace('dict(', '').replace(')', '')
                    doc_key[attribute] = CommentedMap()
                    doc_key[attribute]['description'] = string_list
                    doc_key[attribute]['type'] = 'complex'
                    sub_obj = None
                    try:
                        sub_obj = getattr(models, class_name)()
                    except:
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

    @property
    def examples(self):
        """ Generate EXAMPLES doc string by matching the API version and model name to a YAML file found in
             ./examples """
        result = []
        result_str = ''
        # check if an example file exists
        file_name = "{0}_{1}.yml".format(self.api_version.lower(),
                                         self.helper.base_model_name_snake)
        example_path = os.path.join(os.path.dirname(__file__), 'examples', file_name)
        if os.path.exists(example_path):
            logger.debug('parsing {}'.format(example_path))
            yaml_examples = ruamel.yaml.load(open(example_path, 'r'), Loader=ruamel.yaml.RoundTripLoader)
            for ex in yaml_examples:
                new_example = CommentedMap()
                for key, value in ex.items():
                    if key == 'name':
                        # Add name as the first key in new_example
                        new_example['name'] = value

                for key, value in ex.items():
                    if key != 'name':
                        # Add the module name as the second key
                        module_name = 'k8s_{0}_{1}'.format(self.api_version.lower(),
                                                           self.helper.base_model_name_snake)
                        new_example[module_name] = value
                        if 'state' in self.helper.argspec:
                            # Add a state parameter to the example, placing it after the namespace parameter, or name,
                            #  if no namespace.
                            new_example[module_name] = CommentedMap()
                            if isinstance(value, type(CommentedMap())):
                                params = list(value.keys())
                                i = 0
                                add_after = 'name'
                                if 'namespace' in params:
                                    add_after = 'namespace'
                                if key in ('create', 'patch'):
                                    state = 'present'
                                elif key == 'replace':
                                    state = 'replaced'
                                else:
                                    state = 'absent'

                                while i < len(params):
                                    new_example[module_name][params[i]] = value[params[i]]
                                    if params[i] == add_after:
                                        new_example[module_name]['state'] = state
                                    i += 1

                if new_example.get('name'):
                    result.append(new_example)

        if len(result):
            result_str = ruamel.yaml.dump(result, Dumper=ruamel.yaml.RoundTripDumper, width=80)
            result_str = re.sub('\n- name:', '\n\n- name:', result_str)

        return result_str

    @staticmethod
    def __doc_clean_up(doc_strings):
        def _split_words(l):
            # Split a line into whitespace separated words
            lex = shlex.shlex(l)
            lex.whitespace_split = True
            lex.quotes = ''
            return list(lex)

        def _remove_more_info(l):
            # Remove 'More info: http...'
            words = _split_words(l)
            i = 0
            while i < len(words) - 1:
                if words[i] == 'More' and words[i + 1] == 'info:':
                    i += 2
                    words.pop(i)
                    words.pop(i - 1)
                    words.pop(i - 2)
                    break
                i += 1
            return ' '.join(words)

        def _remove_link(l):
            words = _split_words(l)
            i = 0
            while i <= len(words) - 1:
                if 'https://' in words[i]:
                    words.pop(i)
                    break
                i += 1
            return ' '.join(words)

        result = []
        for line in doc_strings:
            if re.match(':', line):
                continue
            if line == '':
                continue
            if re.match('Gets the', line) or re.match('Sets the', line):
                continue
            line = _remove_more_info(line)
            line = _remove_link(line)
            result.append(line)
        return result


