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

# Generates client.
# Required env vars:
#   CLEANUP_DIRS: List of directories to cleanup before generation for this language
#   KUBERNETES_BRANCH: Kubernetes branch name to get the swagger spec from
#   CLIENT_VERSION: Client version. Will be used in the comment sections of the generated code
#   PACKAGE_NAME: Name of the client package.
#   CLIENT_LANGUAGE: Language of the client. ${CLIENT_LANGUAGE}.xml should exists.
# Optional env vars:
#   SWAGGER_CODEGEN_COMMIT: swagger-codegen-version
# Input vars:
#   $1: output directory
kubeclient::generator::generate_client() {
    : "${CLEANUP_DIRS?Must set CLEANUP_DIRS env var}"
    : "${KUBERNETES_BRANCH?Must set KUBERNETES_BRANCH env var}"
    : "${CLIENT_VERSION?Must set CLIENT_VERSION env var}"
    : "${PACKAGE_NAME?Must set PACKAGE_NAME env var}"
    : "${CLIENT_LANGUAGE?Must set CLIENT_LANGUAGE env var}"

    SWAGGER_CODEGEN_COMMIT="${SWAGGER_CODEGEN_COMMIT:-v2.2.3}"

    local output_dir=$1
    pushd "${output_dir}" > /dev/null
    local output_dir=`pwd`
    popd > /dev/null
    SCRIPT_ROOT=$(dirname "${BASH_SOURCE}")
    pushd "${SCRIPT_ROOT}" > /dev/null
    local SCRIPT_ROOT=`pwd`
    popd > /dev/null

    mkdir -p "${output_dir}"

    echo "--- Building docker image..."
    docker build "${SCRIPT_ROOT}" -t "kubernetes-${CLIENT_LANGUAGE}-client-gen:v1" \
        --build-arg SWAGGER_CODEGEN_COMMIT="${SWAGGER_CODEGEN_COMMIT}" \
        --build-arg GENERATION_XML_FILE="${CLIENT_LANGUAGE}.xml"

    # Docker does not support passing arrays, pass the string representation
    # of the array instead (space separated)
    CLEANUP_DIRS_STRING="${CLEANUP_DIRS[@]}"

    echo "--- Running generator inside container..."
    docker run \
        -e CLEANUP_DIRS="${CLEANUP_DIRS_STRING}" \
        -e KUBERNETES_BRANCH="${KUBERNETES_BRANCH}" \
        -e CLIENT_VERSION="${CLIENT_VERSION}" \
        -e CLIENT_LANGUAGE="${CLIENT_LANGUAGE}" \
        -e PACKAGE_NAME="${PACKAGE_NAME}" \
        -e SWAGGER_CODEGEN_COMMIT="${SWAGGER_CODEGEN_COMMIT}" \
        -v "${output_dir}:/output_dir:Z" \
        "kubernetes-${CLIENT_LANGUAGE}-client-gen:v1" "/output_dir"

    echo "---Done."
}
