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

FROM maven:3.5-jdk-7
ARG SWAGGER_CODEGEN_COMMIT
ARG GENERATION_XML_FILE
ARG SWAGGER_CODEGEN_USER_ORG=swagger-api

# Install preprocessing script requirements
RUN apt-get update && apt-get -y install python-pip && pip install urllib3 kubernetes python-string-utils

# Check out specific commit of swagger-codegen
RUN mkdir /source && \
    cd /source && \
    git clone -n https://github.com/${SWAGGER_CODEGEN_USER_ORG}/swagger-codegen.git && \
    cd swagger-codegen && \
    git checkout $SWAGGER_CODEGEN_COMMIT

# Build it and persist local repository
RUN cd /source/swagger-codegen && \
    mvn install -DskipTests -Dmaven.test.skip=true -pl modules/swagger-codegen-maven-plugin -am && \
    cp -r /root/.m2/* /usr/share/maven/ref

# Copy required files
COPY ${GENERATION_XML_FILE} /generation_params.xml
COPY generate_client_in_container.sh /generate_client.sh
COPY preprocess_spec.py /
COPY custom_objects_spec.json /

ENTRYPOINT ["mvn-entrypoint.sh", "/generate_client.sh"]
