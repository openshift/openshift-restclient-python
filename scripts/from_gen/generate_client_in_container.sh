#!/bin/bash

# Copyright 2017 The Kubernetes Authors.
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

# Generates client.
# Required env vars:
#   CLEANUP_DIRS: List of directories (string separated by space) to cleanup before generation for this language
#   KUBERNETES_BRANCH: Kubernetes branch name to get the swagger spec from
#   CLIENT_VERSION: Client version. Will be used in the comment sections of the generated code
#   PACKAGE_NAME: Name of the client package.
#   SWAGGER_CODEGEN_COMMIT: swagger-codegen commit sha or tag/branch name. Will only be used as a reference in docs.
# Input vars:
#   $1: output directory
: "${CLEANUP_DIRS?Must set CLEANUP_DIRS env var}"
: "${KUBERNETES_BRANCH?Must set KUBERNETES_BRANCH env var}"
: "${CLIENT_VERSION?Must set CLIENT_VERSION env var}"
: "${CLIENT_LANGUAGE?Must set CLIENT_LANGUAGE env var}"
: "${PACKAGE_NAME?Must set PACKAGE_NAME env var}"
: "${SWAGGER_CODEGEN_COMMIT?Must set SWAGGER_CODEGEN_COMMIT env var}"

output_dir=$1
pushd "${output_dir}" > /dev/null
output_dir=`pwd`
popd > /dev/null
SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
pushd "${SCRIPT_ROOT}" > /dev/null
SCRIPT_ROOT=`pwd`
popd > /dev/null

if ! which mvn > /dev/null 2>&1; then
    echo "Maven is not installed."
    exit
fi

# There should be only one version of swagger-codegen-maven-plugin.
unset PLUGIN_VERSION
shopt -s nullglob
FOLDERS=(/root/.m2/repository/io/swagger/swagger-codegen-maven-plugin/*)
for folder in "${FOLDERS[@]}"; do
    if [[ -d "${folder}" ]]; then
        folder=$(basename "${folder}")
        if [[ ! -z "${PLUGIN_VERSION:-}" ]]; then
            echo "Multiple swagger-codegen-maven-plugin version exists: ${PLUGIN_VERSION} & ${folder}"
            exit 1
        fi
        PLUGIN_VERSION="${folder}"
    fi
done
if [[ -z "${PLUGIN_VERSION:-}" ]]; then
    echo "Cannot find swagger-codegen-maven-plugin version"
    exit 1
fi
shopt -u nullglob

# To make sure we can reproduce generation, we would also log code-gen exact commit
pushd /source/swagger-codegen
  SWAGGER_CODEGEN_COMMIT_ACTUAL=$(git rev-parse HEAD)
popd

mkdir -p "${output_dir}"

echo "--- Downloading and pre-processing OpenAPI spec"
python "${SCRIPT_ROOT}/preprocess_spec.py" "${CLIENT_LANGUAGE}" "${KUBERNETES_BRANCH}" "${output_dir}/swagger.json"

echo "--- Cleaning up previously generated folders"
for i in ${CLEANUP_DIRS}; do
    echo "--- Cleaning up ${output_dir}/${i}"
    rm -rf "${output_dir}/${i}"
done

echo "--- Generating client ..."
mvn -f "${SCRIPT_ROOT}/generation_params.xml" clean generate-sources -Dgenerator.spec.path="${output_dir}/swagger.json" -Dgenerator.output.path="${output_dir}" -D=generator.client.version="${CLIENT_VERSION}" -D=generator.package.name="${PACKAGE_NAME}" -D=swagger-codegen-version="${PLUGIN_VERSION}"

mkdir -p "${output_dir}/.swagger-codegen"
echo "Requested Commit: ${SWAGGER_CODEGEN_COMMIT}" > "${output_dir}/.swagger-codegen/COMMIT"
echo "Actual Commit: ${SWAGGER_CODEGEN_COMMIT_ACTUAL}" >> "${output_dir}/.swagger-codegen/COMMIT"

echo "---Done."
chown -R $(stat -c "%u:%g" ${output_dir}) ${output_dir}
