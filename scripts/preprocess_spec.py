# Copyright 2016 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, print_function

import codecs
import io
import json
import operator
import os.path
import re
import string_utils
import sys
from collections import OrderedDict

import urllib3

from constants import KUBERNETES_BRANCH, SPEC_VERSION, PACKAGE_NAME

# these four constants are shown as part of this example in []:
# "[watch]Pod[List]" is the deprecated version of "[list]Pod?[watch]=True"
WATCH_OP_PREFIX = "watch"
WATCH_OP_SUFFIX = "List"
LIST_OP_PREFIX = "list"
WATCH_QUERY_PARAM_NAME = "watch"

SPEC_URL = 'https://raw.githubusercontent.com/openshift/origin/' \
           '%s/api/swagger-spec/openshift-openapi-spec.json' % KUBERNETES_BRANCH

SCRIPT_DIR = os.path.dirname(__file__)
OUTPUT_PATH = os.path.join(SCRIPT_DIR, 'swagger.json')
CODEGEN_IGNORE_PATH = os.path.join(SCRIPT_DIR, '..', PACKAGE_NAME, '.swagger-codegen-ignore')
VERSION_RX = re.compile("V\d((alpha|beta)\d)?")

_ops = ['get', 'put', 'post', 'delete', 'options', 'head', 'patch']


class PreprocessingException(Exception):
    pass


def apply_func_to_spec_operations(spec, func, **kwargs):
    """Apply func to each operation in the spec.

    :param spec: The OpenAPI spec to apply func to.
    :param func: the function to apply to the spec's operations. It should be
                 a func(operation, parent) where operation will be each
                 operation of the spec and parent would be the parent object of
                 the given operation.
                 If the return value of the func is True, then the operation
                 will be deleted from the spec.
    """
    for k in list(spec['paths'].keys()):
        v = spec['paths'][k]
        for op in _ops:
            if op not in v:
                continue
            if func(v[op], v, path=k, **kwargs):
                del v[op]


def _has_property(prop_list, property_name, **kwargs):
    for prop in prop_list:
        if prop["name"] == property_name:
            return True


def remove_watch_operations(op, parent, operation_ids=None, **kwargs):
    op_id = op['operationId']
    if not op_id.startswith(WATCH_OP_PREFIX):
        return
    list_id = (LIST_OP_PREFIX +
               op_id.replace(WATCH_OP_SUFFIX, "")[len(WATCH_OP_PREFIX):])
    if list_id not in operation_ids:
        raise PreprocessingException("Cannot find %s" % list_id)
    list_op = operation_ids[list_id]
    params = []
    if 'parameters' in list_op:
        params += list_op['parameters']
    if 'parameters' in parent:
        params += parent['parameters']
    if not _has_property(params, WATCH_QUERY_PARAM_NAME):
        raise PreprocessingException("%s has no watch query param" % list_id)
    return True


def strip_tags_from_operation_id(operation, _, **kwargs):
    operation_id = operation['operationId']
    if 'tags' in operation:
        for t in operation['tags']:
            operation_id = operation_id.replace(string_utils.snake_case_to_camel(t), '')
        operation['operationId'] = operation_id


def add_missing_openshift_tags_to_operation(op, _, path=None, **kwargs):
    tags = op.get('tags', [])
    if not tags:
        path_parts = path.split('/')
        if '.openshift.io' in path:
            api_group = path_parts[2].replace('.', '_')
            version = path_parts[3] if VERSION_RX.match(path_parts[3]) else None
        elif 'oapi' in path:
            api_group = path_parts[1]
            version = None
        else:
            raise Exception('Do not know how to process missing tag for path: {}'.format(path))

        tag = api_group
        if version is not None:
            tag += '_' + version
        op['tags'] = [tag]


def update_codegen_ignore(spec):
    with io.open(CODEGEN_IGNORE_PATH) as f:
        ignore_lines = set(f.read().splitlines())

    import kubernetes
    k8s_apis = dir(kubernetes.client.apis)
    k8s_models = dir(kubernetes.client.models)

    api_modules = set()
    model_modules = set()

    for path in list(spec['paths'].values()):
        for op_name in list(path.keys()):
            if op_name != 'parameters':
                op = path[op_name]
                for tag in op['tags']:
                    tag = '_'.join([string_utils.camel_case_to_snake(x) for x in tag.split('_')])
                    api_modules.add(tag + '_api')

    for model in list(spec['definitions'].keys()):
        module_name = '_'.join([string_utils.camel_case_to_snake(x) for x in model.split('.')])
        model_modules.add(module_name)

    for api_module in api_modules:
        suffix = api_module.split('_')[-1]
        if suffix in ['0', 'pre012'] or api_module in k8s_apis:
            ignore_lines.add('client/apis/{}.py'.format(api_module))

    for model_module in model_modules:
        if model_module in k8s_models:
            ignore_lines.add('client/models/{}.py'.format(model_module))

    with io.open(CODEGEN_IGNORE_PATH, mode='w') as f:
        f.write('\n'.join(sorted(ignore_lines)))


def process_swagger(spec):
    apply_func_to_spec_operations(spec, strip_tags_from_operation_id)

    operation_ids = {}
    apply_func_to_spec_operations(spec, lambda op, _, **kwargs: operator.setitem(
        operation_ids, op['operationId'], op))

    try:
        apply_func_to_spec_operations(
            spec, remove_watch_operations, operation_ids=operation_ids)
    except PreprocessingException as e:
        print(str(e))

    apply_func_to_spec_operations(spec, add_missing_openshift_tags_to_operation)
    update_codegen_ignore(spec)

    # TODO: Kubernetes does not set a version for OpenAPI spec yet,
    # remove this when that is fixed.
    spec['info']['version'] = SPEC_VERSION

    return spec


def main():
    pool = urllib3.PoolManager()
    reader = codecs.getreader('utf-8')
    with pool.request('GET', SPEC_URL, preload_content=False) as response:
        if response.status != 200:
            print("Error downloading spec file. Reason: %s" % response.reason)
            return 1
        in_spec = json.load(reader(response), object_pairs_hook=OrderedDict)
        out_spec = process_swagger(in_spec)
        with open(OUTPUT_PATH, 'w') as out:
            json.dump(out_spec, out, sort_keys=False, indent=2,
                      separators=(',', ': '), ensure_ascii=True)
    return 0


sys.exit(main())
