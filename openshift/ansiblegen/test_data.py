# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import logging

from openshift.client import models
from openshift.helper import OpenShiftException
from openshift.helper.ansible import AnsibleModuleHelper

logger = logging.getLogger(__name__)


class TestData(object):

    def __init__(self, model, api_version):
        self.model = model
        self.api_version = api_version
        try:
            self.helper = AnsibleModuleHelper(self.api_version, self.model)
        except OpenShiftException:
            raise

    def create_object(self):
        result = dict(create=dict(), name="Create {}".format(self.helper.base_model_name_snake))
        params = dict()
        for arg_key, arg_value in self.helper.argspec.items():
            if arg_value.get('property_path'):
                if arg_value.get('type') == 'str' or arg_value.get('type') is None:
                    params[arg_key] = 'foo'
                if arg_value.get('type') == 'int':
                    params[arg_key] = 1
                if arg_value.get('type') == 'bool':
                    params[arg_key] = True
                if arg_value.get('type') == 'list':
                    list_type = self.__get_list_type(arg_value['property_path'])
                    if list_type  == 'str':
                        params[arg_key] = 'foo'
                    elif list_type == 'int':
                        params[arg_key] = 1
                    elif list_type == 'bool':
                        params[arg_key] = True
                    elif list_type == 'dict':
                        params[arg_key] = {}
                    else:
                        params[arg_key] = dict()
                        new_obj = getattr(models, list_type)()

                self.__build_args(params[arg_key], arg_value.get('type'), arg_value['property_path'])

    def __build_args(self, param, param_type, property_path):
        if param_type == 'str' or param_type is None:
            param = 'foo'
        if param_type == 'int':
            param = 1
        if param_type == 'bool':
            param = True
        if param_type == 'list':
            list_type = self.__get_list_type(property_path)
            if list_type  == 'str':
                param = ['foo']
            elif list_type == 'int':
                param = [1]
            elif list_type == 'bool':
                param = [True]
            elif list_type == 'dict':
                param = [{}]
            else:
                param = dict()
                obj_class = getattr(models, list_type)
                properties = [x for x in dir(obj_class) if isinstance(getattr(obj_class, x), property)]

    def __get_list_type(self, property_path):
        current_obj = self.helper.model()
        result = None
        for path in property_path:
            prop_type = current_obj.swagger_types[path]
            if prop_type in ('str', 'int', 'bool'):
                continue
            elif prop_type.startswith('dict('):
                continue
            elif prop_type.startswith('list['):
                list_type = current_obj.swagger_types[path].replace('list[').replace(']')
                result = list_type
                break
            current_obj = getattr(models, prop_type)()
        return result



