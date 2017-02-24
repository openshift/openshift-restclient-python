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
from openshift.helper import OpenShiftException, VERSION_RX
from .docstrings import DocStrings

logger = logging.getLogger(__name__)

# Once the modules land in Ansible core, this should not change
ANSIBLE_VERSION_ADDED = "2.3.0"


class Modules(object):

    def __init__(self, **kwargs):
        self.api_version = kwargs.pop('api_version')
        self.output_path = os.path.normpath(kwargs.pop('output_path'))
        self.suppress_stdout = kwargs.pop('suppress_stdout')
        self.template_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'templates'))

        logger.debug("output_path: {}".format(self.output_path))

        # Evaluate openshift.models.*, and determine which models should be a module
        self.models = []
        requested_models = kwargs.pop('models')
        for model, model_class in inspect.getmembers(openshift_models):
            if 'kind' in dir(model_class) and 'metadata' in dir(model_class):
                # models with a 'kind' are top-level objects that we care about
                matches = VERSION_RX.match(model)
                if not matches:
                    # exclude unversioned models
                    continue
                model_api = matches.group(0)
                base_model_name = model.replace(model_api, '')
                model_name_snake = string_utils.camel_case_to_snake(base_model_name)
                if requested_models and \
                   base_model_name not in requested_models and \
                   model_name_snake not in requested_models:
                    continue
                if self.api_version:
                    # only include models for the requested API version
                    if model_api == self.api_version.capitalize():
                        self.models.append({
                            'model': model,
                            'model_api': model_api,
                            'base_model_name': base_model_name,
                            'model_name_snake': model_name_snake
                        })
                else:
                    self.models.append({
                        'model': model,
                        'model_api': model_api,
                        'base_model_name': base_model_name,
                        'model_name_snake': model_name_snake
                    })

    def generate_modules(self):
        """
        Create requested Ansible modules, writing them to self.output_path.

        :return: None
        """
        self.__create_output_path()
        temp_dir = os.path.realpath(tempfile.mkdtemp())  # jinja temp dir
        for model in self.models:
            module_name = "k8s_{0}_{1}.py".format(model['model_api'].lower(),
                                                  model['model_name_snake'])
            if not self.suppress_stdout:
                print(module_name)
            docs = DocStrings(model['model_name_snake'], model['model_api'])

            try:
                logger.debug("get docs for {}".format(model['model_name_snake']))
                documentation = docs.documentation
                logger.debug("success!")
            except Exception as exc:
                logger.debug("failed!!")
                raise OpenShiftException(exc.message)

            context = {
                'documentation_string': documentation,
                'return_string': docs.return_block,
                'kind': model['model_name_snake'],
                'api_version': model['model_api']
            }
            self.__jinja_render_to_temp('k8s_module.j2', module_name, temp_dir, **context)
            if not self.suppress_stdout:
                sys.stdout.write("\033[F") # cursor up 1 line
                sys.stdout.write("\033[K") # clear to EOL
        shutil.rmtree(temp_dir)
        if not self.suppress_stdout:
            print("Generated {} modules".format(len(self.models)))

    def __jinja_render_to_temp(self, template_file, module_name, temp_dir, **context):
        """
        Create the module from a jinja template.

        :param template_file: name of the template file
        :param module_name: the destination file name
        :param temp_dir: a temporary working dir for jinja
        :param context: dict of substitution variables
        :return: None
        """
        j2_tmpl_path = self.template_path
        j2_env = Environment(loader=FileSystemLoader(j2_tmpl_path))
        j2_tmpl = j2_env.get_template(template_file)
        rendered = j2_tmpl.render(dict(temp_dir=temp_dir, **context))
        with open(os.path.normpath(os.path.join(self.output_path, module_name)), 'wb') as f:
            f.write(rendered.encode('utf8'))

    def __create_output_path(self):
        """
        Attempt to create the output path, if it does not already exist

        :return: None
        """
        if os.path.exists(self.output_path):
            if not os.path.isdir(self.output_path):
                raise OpenShiftException("ERROR: expected {} to be a directory.".format(self.output_path))
        else:
            try:
                os.makedirs(self.output_path, 0775)
            except os.error as exc:
                raise OpenShiftException("ERROR: could not create {0} - {1}".format(self.output_path, str(exc)))
