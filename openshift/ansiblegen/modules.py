# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function

import logging
import inspect
import os
import re
import shutil
import string_utils
import sys
import tempfile

from jinja2 import Environment, FileSystemLoader

from openshift.client import models as openshift_models
from openshift.helper import OpenShiftException, METACLASS_NAME
from .docstrings import DocStrings

logger = logging.getLogger(__name__)

# Once the modules land in Ansible core, this should not change
ANSIBLE_VERSION_ADDED = "2.3.0"


class Modules(object):

    def __init__(self, **kwargs):
        self.models = kwargs.pop('models')
        self.api_version = kwargs.pop('api_version')
        self.output_path = os.path.normpath(kwargs.pop('output_path'))
        self.suppress_stdout = kwargs.pop('suppress_stdout')
        self.template_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'templates'))

        logger.debug("output_path: {}".format(self.output_path))

        if not self.models:
            self.models = []
            for model, model_class in inspect.getmembers(openshift_models):
                if 'kind' in dir(model_class):
                    obj = model_class()
                    if obj.swagger_types.get('metadata') == METACLASS_NAME:
                        # only models that have a kind, and the expected metaclass
                        if self.api_version:
                            m = re.match(r'V\d{1,2}((alpha|beta)\d{1,2})?', model)
                            model_api = m.group(0)
                            # only grab things that start with the requested version
                            if model_api == self.api_version.capitalize():
                                self.models.append(model)
                        else:
                            if not model.startswith('Unversioned'):
                                self.models.append(model)

    def generate_modules(self):
        """
        Create requested Ansible modules, writing them to self.output_path.

        :return: None
        """
        self.__create_output_path()
        temp_dir = os.path.realpath(tempfile.mkdtemp())
        for model_name in self.models:
            # Get the model's API
            m = re.match(r'V\d{1,2}((alpha|beta)\d{1,2})?', model_name)
            if not m:
                raise OpenShiftException(
                    "ERROR: Encountered model {}, which does not have a recognized version".format(model_name)
                )
            model_api = m.group(0)
            base_model_name = model_name.replace(model_api, '')
            model_name_snake = string_utils.camel_case_to_snake(base_model_name)
            module_name = "k8s_{0}_{1}.py".format(model_api.lower(), model_name_snake)
            if not self.suppress_stdout:
                print(module_name)
            docs = DocStrings(model_name_snake, model_api)
            context = {
                'documentation_string': docs.documentation,
                'return_string': docs.return_block,
                'kind': model_name_snake,
                'api_version': model_api
            }
            self.__jinja_render_to_temp('k8s_module.j2', module_name, temp_dir, **context)
            if not self.suppress_stdout:
                sys.stdout.write("\033[F") # cursor up 1 line
                sys.stdout.write("\033[K") # clear to EOL

        shutil.rmtree(temp_dir)
        if not self.suppress_stdout:
            print("Generated {} modules".format(len(self.models)))

    def __jinja_render_to_temp(self, template_file, module_name, temp_dir, **context):
        j2_tmpl_path = self.template_path
        j2_env = Environment(loader=FileSystemLoader(j2_tmpl_path))
        j2_tmpl = j2_env.get_template(template_file)
        rendered = j2_tmpl.render(dict(temp_dir=temp_dir, **context))
        with open(os.path.normpath(os.path.join(self.output_path, module_name)), 'wb') as f:
            f.write(rendered.encode('utf8'))

    def __create_output_path(self):
        # Attempt to create the output path, if it does not already exist
        if os.path.exists(self.output_path):
            if not os.path.isdir(self.output_path):
                raise OpenShiftException("ERROR: expected {} to be a directory.".format(self.output_path))
        else:
            try:
                os.makedirs(self.output_path, 0775)
            except os.error as exc:
                raise OpenShiftException("ERROR: could not create {0} - {1}".format(self.output_path, str(exc)))
