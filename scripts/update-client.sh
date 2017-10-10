#!/bin/bash

# Copyright 2015 The Kubernetes Authors.
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

# Script to fetch latest swagger spec.
# Puts the updated spec at api/swagger-spec/

set -x
set -o errexit
set -o nounset
set -o pipefail

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
SOURCE_ROOT="${SCRIPT_ROOT}/../"
CLIENT_ROOT="${SOURCE_ROOT}/${PACKAGE_NAME}"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
KUBERNETES_CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" KUBERNETES_CLIENT_VERSION)
DEVELOPMENT_STATUS=$(python "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

pushd "${SOURCE_ROOT}" > /dev/null
SOURCE_ROOT=`pwd`
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

set +o nounset
if [ -d "${SOURCE_ROOT}/venv" ]; then
  source "${SOURCE_ROOT}/venv/bin/activate"
fi
set -o nounset

TEMP_FOLDER=$(mktemp -d)
# trap "rm -rf ${TEMP_FOLDER}" EXIT SIGINT

SETTING_FILE="${TEMP_FOLDER}/settings"
echo "export KUBERNETES_BRANCH=\"$(python ${SCRIPT_ROOT}/constants.py KUBERNETES_BRANCH)\"" > $SETTING_FILE
echo "export CLIENT_VERSION=\"$(python ${SCRIPT_ROOT}/constants.py CLIENT_VERSION)\"" >> $SETTING_FILE
echo "export PACKAGE_NAME=\"client\"" >> $SETTING_FILE


echo ">>> Running python generator from the gen repo"
"${SCRIPT_ROOT}/from_gen/python.sh" "${CLIENT_ROOT}" "${SETTING_FILE}"

mv "${CLIENT_ROOT}/swagger.json" "${SCRIPT_ROOT}/swagger.json"


echo "--- Patching generated code..."
find "${CLIENT_ROOT}/" -type f -name \*.md -exec sed -i "s/${PACKAGE_NAME}.client-python/client-python/g" {} +

echo "--- updating version information..."
sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^__k8s_client_version__ = .*/__k8s_client_version__ = \\\"${KUBERNETES_CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^kubernetes ~= .*/kubernetes ~= ${KUBERNETES_CLIENT_VERSION}/" "${SCRIPT_ROOT}/../requirements.txt"
sed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup.py"
sed -i'' "/^configuration = Configuration()$/d" "${CLIENT_ROOT}/client/__init__.py"
sed -i'' "/^from .configuration import Configuration$/d" "${CLIENT_ROOT}/client/__init__.py"
sed -i '${/^$/d;}' "${CLIENT_ROOT}/client/__init__.py"
sed -i'' "s/^Version:.*/Version:    ${CLIENT_VERSION}/" "${SCRIPT_ROOT}/../python-openshift.spec"
echo "from kubernetes.client.configuration import Configuration, ConfigurationObject, configuration" >> "${CLIENT_ROOT}/client/__init__.py"


echo "--- Patching to use k8s client-python where possible"
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i 's/^from \.\+configuration/from kubernetes.client.configuration/g' {} +
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i 's/^from \.\+rest/from kubernetes.client.rest/g' {} +
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i "s/^from ${PACKAGE_NAME}.client.rest/from kubernetes.client.rest/g" {} +
find "${CLIENT_ROOT}/" -type f -name \*.md -exec sed -i "s/^from ${PACKAGE_NAME}.client.rest/from kubernetes.client.rest/g" {} +


echo "--- Patching auth_settings"
find "${CLIENT_ROOT}/client/apis" -type f -name \*.py -exec sed -i "s/auth_settings = \[\]/auth_settings = \['BearerToken'\]/g" {} +

echo "--- Post processing of generated packages"
python "${SCRIPT_ROOT}/update_generated.py"


echo "---Done."
