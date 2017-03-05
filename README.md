# OpenShift python client

[![Build Status](https://travis-ci.org/openshift/openshift-restclient-python.svg?branch=master)](https://travis-ci.org/openshift/openshift-restclient-python)
[![Coverage Status](https://coveralls.io/repos/github/openshift/openshift-restclient-python/badge.svg?branch=master)](https://coveralls.io/github/openshift/openshift-restclient-python?branch=master)

Python client for the [OpenShift](http://openshift.redhat.com/) API.

## Installation

From source:

```
git clone https://github.com/openshift/openshift-restclient-python.git
cd openshift-restclient-python
python setup.py install
```

From [PyPi](https://pypi.python.org/pypi/openshift/) directly (coming soon):

```
pip install openshift
```

## Example

TODO

## Documentation

All APIs and Models' documentation can be found at the [Generated client's README file](openshift/README.md)

## Community, Support, Discussion

If you have any problem with the package or any suggestions, please file an [issue](https://github.com/openshift/openshift-restclient-python/issues).

### Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).

## Update generated client
Updating the generated client requires the following tools:
- tox
- maven3

1) Incorporate new changes to update scripts
  - scripts/constants.py, scripts/pom.xml, scripts/preprocess_spec.py, update-client.sh are the most important
1) Run tox -e update_client
