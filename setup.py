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
"""
To install the library, run the following

python setup.py install

prerequisite: setuptools
http://pypi.python.org/pypi/setuptools
"""

from setuptools import find_packages, setup

# Do not edit these constants. They will be updated automatically
# by scripts/update-client.sh.
CLIENT_VERSION = "0.8.8"
PACKAGE_NAME = "openshift"
DEVELOPMENT_STATUS = "3 - Alpha"


def extract_requirements(filename):
    """
    Extracts requirements from a pip formatted requirements file.
    """
    with open(filename, 'r') as requirements_file:
        return requirements_file.read().splitlines()


setup(
    name=PACKAGE_NAME,
    version=CLIENT_VERSION,
    description="OpenShift python client",
    author_email="",
    author="OpenShift",
    license="Apache License Version 2.0",
    url="https://github.com/openshift/openshift-restclient-python",
    keywords=["Swagger", "OpenAPI", "Kubernetes", "OpenShift"],
    install_requires=extract_requirements('requirements.txt'),
    packages=find_packages(include='openshift.*'),
    include_package_data=True,
    data_files=[
        ('requirements.txt', ['requirements.txt']),
        ('custom_objects_spec.json',
         ['scripts/from_gen/custom_objects_spec.json']
        )
    ],
    long_description='Python client for OpenShift http://openshift.redhat.com/',
    classifiers=[
        "Development Status :: %s" % DEVELOPMENT_STATUS,
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    entry_points={
        'console_scripts': ['openshift-ansible-gen = openshift.ansiblegen.cli:commandline']
    },
)
