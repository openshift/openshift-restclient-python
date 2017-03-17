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

set -o errexit
set -o nounset
set -o pipefail

if ! which mvn > /dev/null 2>&1; then
  echo "Maven is not installed."
  exit
fi

SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
PACKAGE_NAME=$(python "${SCRIPT_ROOT}/constants.py" PACKAGE_NAME)
CLIENT_ROOT="${SCRIPT_ROOT}/../${PACKAGE_NAME}"
CLIENT_VERSION=$(python "${SCRIPT_ROOT}/constants.py" CLIENT_VERSION)
DEVELOPMENT_STATUS=$(python "${SCRIPT_ROOT}/constants.py" DEVELOPMENT_STATUS)

pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

pushd "${CLIENT_ROOT}" > /dev/null
CLIENT_ROOT=`pwd`
popd > /dev/null

echo "--- Downloading and processing OpenAPI spec"
python "${SCRIPT_ROOT}/preprocess_spec.py"

echo "--- Cleaning up previously generated folders"
rm -rf "${CLIENT_ROOT}/client/apis"
rm -rf "${CLIENT_ROOT}/client/models"
rm -rf "${CLIENT_ROOT}/docs"
rm -rf "${CLIENT_ROOT}/test"

echo "--- Generating client ..."
mvn -f "${SCRIPT_ROOT}/pom.xml" clean generate-sources -Dgenerator.spec.path="${SCRIPT_ROOT}/swagger.json" -Dgenerator.output.path="${CLIENT_ROOT}" -Dgenerator.package.name=client -D=generator.client.version=${CLIENT_VERSION}

echo "--- Patching generated code..."
find "${CLIENT_ROOT}/test" -type f -name \*.py -exec sed -i "s/\bclient/${PACKAGE_NAME}.client/g" {} +
find "${CLIENT_ROOT}/" -type f -name \*.md -exec sed -i "s/\bclient/${PACKAGE_NAME}.client/g" {} +
find "${CLIENT_ROOT}/" -type f -name \*.md -exec sed -i "s/${PACKAGE_NAME}.client-python/client-python/g" {} +
# rm "${CLIENT_ROOT}/LICENSE"
echo "--- updating version information..."
#sed -i'' "s/^CLIENT_VERSION = .*/CLIENT_VERSION = \\\"${CLIENT_VERSION}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s/^__version__ = .*/__version__ = \\\"${CLIENT_VERSION}\\\"/" "${CLIENT_ROOT}/__init__.py"
sed -i'' "s/^PACKAGE_NAME = .*/PACKAGE_NAME = \\\"${PACKAGE_NAME}\\\"/" "${SCRIPT_ROOT}/../setup.py"
sed -i'' "s,^DEVELOPMENT_STATUS = .*,DEVELOPMENT_STATUS = \\\"${DEVELOPMENT_STATUS}\\\"," "${SCRIPT_ROOT}/../setup.py"
sed -i'' "/^configuration = Configuration()$/d" "${CLIENT_ROOT}/client/__init__.py"
sed -i'' "/^from .configuration import Configuration$/d" "${CLIENT_ROOT}/client/__init__.py"
sed -i '${/^$/d;}' "${CLIENT_ROOT}/client/__init__.py"
echo "from kubernetes.client.configuration import Configuration, ConfigurationObject, configuration" >> "${CLIENT_ROOT}/client/__init__.py"


echo "--- Patching to use k8s client-python where possible"
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i 's/^from \.\+configuration/from kubernetes.client.configuration/g' {} +
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i 's/^from \.\+rest/from kubernetes.client.rest/g' {} +
find "${CLIENT_ROOT}/" -type f -name \*.py -exec sed -i "s/^from ${PACKAGE_NAME}.client.rest/from kubernetes.client.rest/g" {} +
find "${CLIENT_ROOT}/" -type f -name \*.md -exec sed -i "s/^from ${PACKAGE_NAME}.client.rest/from kubernetes.client.rest/g" {} +


echo "--- Patching auth_settings"
find "${CLIENT_ROOT}/client/apis" -type f -name \*.py -exec sed -i "s/auth_settings = \[\]/auth_settings = \['BearerToken'\]/g" {} +


echo "---Done."
