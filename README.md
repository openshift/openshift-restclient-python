OpenShift python client
======================

[![Build Status](https://travis-ci.com/openshift/openshift-restclient-python.svg?branch=master)](https://travis-ci.com/openshift/openshift-restclient-python)
[![Coverage Status](https://coveralls.io/repos/github/openshift/openshift-restclient-python/badge.svg?branch=master)](https://coveralls.io/github/openshift/openshift-restclient-python?branch=master)

Python client for the [Kubernetes](https://kubernetes.io/) and [OpenShift](http://openshift.redhat.com/) APIs.

There are two ways this project interacts with the Kubernetes and OpenShift APIs.
The first, **now deprecated**, is to use models and functions generated with
swagger from the API spec. The second, new approach, is to use a single model
and client to generically interact with all resources on the server. The
dynamic client also works with resources that are defined by aggregated
API servers or Custom Resource Definitions.

# Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Examples](#examples)
  * [Create a Service](#create-a-service)
  * [Create a Route](#create-a-route)
  * [List Projects](#list-projects)
  * [Custom Resources](#custom-resources)
  * [OpenShift Login with username and password](#openshift-login-with-username-and-password)
* [Available Methods for Resources](#available-methods-for-resources)
  * [Get](#get)
  * [Create](#create)
  * [Delete](#delete)
  * [Patch](#patch)
  * [Replace](#replace)
  * [Watch](#watch)
* [Community, Support, Discussion](#community-support-discussion)
* [Code of Conduct](#code-of-conduct)

# Installation

From source:

```
git clone https://github.com/openshift/openshift-restclient-python.git
cd openshift-restclient-python
python setup.py install
```

From [PyPi](https://pypi.python.org/pypi/openshift/) directly:

```
pip install openshift
```

Using [Dockerfile](Dockerfile):

```
docker build -t openshift-restclient-python -f Dockerfile .
```

# Usage

The OpenShift client depends on the [Kubernetes Python
client](https://github.com/kubernetes-incubator/client-python.git), and as part
of the installation process, the Kubernetes (K8s) client is automatically
installed.

In the case you are using Docker, you will likely need to share your
`.kube/config` with the `openshift-restclient-python` container:

```
docker run -it -v $HOME/.kube/config:/root/.kube/config:z openshift-restclient-python python
```

To work with the dynamic client, you will need an instantiated Kubernetes
client object. The Kubernetes client object requires a Kubernetes Config
that can be set in the [Config
class](https://github.com/kubernetes-client/python/blob/master/kubernetes/client/configuration.py)
or using a helper utility.  All of the examples that follow make use of the
`new_client_from_config()` helper utility provided by the [Kubernetes Client
Config](https://github.com/kubernetes-client/python-base/blob/master/config/kube_config.py)
that returns an API client to be used with any API object.
There are plenty of [Kubernetes Client
examples](https://github.com/kubernetes-client/python/tree/master/examples) to
examine other ways of accessing Kubernetes Clusters.

# Examples

## Create a Service

```python
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

service = """
kind: Service
apiVersion: v1
metadata:
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 8080
    targetPort: 9376
"""

service_data = yaml.load(service)
resp = v1_services.create(body=service_data, namespace='default')

# resp is a ResourceInstance object
print(resp.metadata)
```

## Create a Route

Now, we create a Route object, and associate it with the Service from our
previous example:

```python
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_routes = dyn_client.resources.get(api_version='route.openshift.io/v1', kind='Route')

route = """
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: frontend
spec:
  host: www.example.com
  to:
    kind: Service
    name: my-service
"""

route_data = yaml.load(route)
resp = v1_routes.create(body=route_data, namespace='default')

# resp is a ResourceInstance object
print(resp.metadata)
```

## List Projects

The following uses the dynamic client to list Projects the user can access:

```python
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')

project_list = v1_projects.get()

for project in project_list.items:
    print(project.metadata.name)
```

## Custom Resources

In the following example, we first create a Custom
Resource Definition for `foos.bar.com`, then create an `Foo` resource,
and finally get a list of `Foo` resources:

```python
import yaml
from kubernetes import client, config
from openshift.dynamic import DynamicClient

k8s_client = config.new_client_from_config()
dyn_client = DynamicClient(k8s_client)

custom_resources = dyn_client.resources.get(
  api_version='apiextensions.k8s.io/v1beta1',
  kind='CustomResourceDefinition'
)

# Define the Foo Resource
foo_crd = """
kind: CustomResourceDefinition
apiVersion: apiextensions.k8s.io/v1beta1
metadata:
  name: foos.bar.com
spec:
  group: bar.com
  names:
    kind: Foo
    listKind: FooList
    plural: foos
    shortNames:
    - foo
    singular: foo
  scope: Namespaced
  version: v1beta1
"""
custom_resources.create(body=yaml.load(foo_crd))

foo_resources = None
while not foo_resources:
  try:
    # Notice the re-instantiation of the dynamic client as a new resource has been created.
    dyn_client = DynamicClient(k8s_client)
    foo_resources = dyn_client.resources.get(api_version='bar.com/v1beta1', kind='Foo')
  except:
    pass

# Create the Foo Resource
foo_resource_cr = """
kind: Foo
apiVersion: bar.com/v1beta1
metadata:
  name: example-foo
  namespace: default
spec:
  version: 1
"""
foo_resources.create(body=yaml.load(foo_resource_cr))

for item in foo_resources.get().items:
  print(item.metadata.name)
```

## OpenShift Login with username and password

```python
from kubernetes import client
from openshift.dynamic import DynamicClient
from openshift.helper.userpassauth import OCPLoginConfiguration
 
apihost = 'https://api.cluster.example.com:6443'
username = 'demo-user'
password = 'insecure'
 
kubeConfig = OCPLoginConfiguration(ocp_username=username, ocp_password=password)
kubeConfig.host = apihost
kubeConfig.verify_ssl = True
kubeConfig.ssl_ca_cert = './ocp.pem' # use a certificate bundle for the TLS validation
 
# Retrieve the auth token
kubeConfig.get_token()
 
print('Auth token: {0}'.format(kubeConfig.api_key))
print('Token expires: {0}'.format(kubeConfig.api_key_expires))
 
k8s_client = client.ApiClient(kubeConfig)
 
dyn_client = DynamicClient(k8s_client)
v1_projects = dyn_client.resources.get(api_version='project.openshift.io/v1', kind='Project')
project_list = v1_projects.get()
 
for project in project_list.items:
    print(project.metadata.name)
 
# Renew the auth token
kubeConfig.get_token()
 
print('Auth token: {0}'.format(kubeConfig.api_key))
print('Token expires: {0}'.format(kubeConfig.api_key_expires))
```

# Available Methods for Resources

The generic Resource class supports the following methods, though every resource kind does not support every method.


## Get

`get(name=None, namespace=None, label_selector=None, field_selector=None, **kwargs)`

Query for a resource in the cluster. Will return a `ResourceInstance` object or raise a `NotFoundError`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

# Gets the specific Service named 'example' from the 'test' namespace
v1_services.get(name='example', namespace='test')

# Lists all Services in the 'test' namespace
v1_services.get(namespace='test')

# Lists all Services in the cluster (requires high permission level)
v1_services.get()

# Gets all Services in the 'test' namespace with the 'app' label set to 'foo'
v1_services.get(namespace='test', label_selector='app=foo')

# Gets all Services except for those in the 'default' namespace
v1_services.get(field_selector='metadata.namespace!=default')

```

`get(body=None, namespace=None, **kwargs)`

Query for a resource in the cluster. Will return a `ResourceInstance` object or raise a `NotFoundError`

For List kind resources (ie, the resource name ends in `List`), the `get` implementation is slightly different.
Rather than taking a name, they take a `*List` kind definition and call `get` for each definition in the list.

```python
v1_service_list = dyn_client.resources.get(api_version='v1', kind='ServiceList')

body = {
    'kind': 'ServiceList',
    'apiVersion': 'v1',
    'items': [
        'metadata': {'name': 'my-service'},
        'spec': {
            'selector': {'app': 'MyApp'},
            'ports': [{
                'protocol': 'TCP',
                'port': '8080',
                'targetPort': '9376'
            }]
        }
    ],
    # More definitions would go here
}
# Gets the specified Service(s) from the 'test' namespace
v1_service_list.get(body=body, namespace='test')

# Lists all Services in the 'test' namespace
v1_service_list.get(namespace='test')

# Lists all Services in the cluster (requires high permission level)
v1_service_list.get()
```

## Create

`create(body=None, namespace=None, **kwargs)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

body = {
    'kind': 'Service',
    'apiVersion': 'v1',
    'metadata': {'name': 'my-service'},
    'spec': {
        'selector': {'app': 'MyApp'},
        'ports': [{
            'protocol': 'TCP',
            'port': '8080',
            'targetPort': '9376'
        }]
    }
}

# Creates the above service in the 'test' namespace
v1_services.create(body=body, namespace='test')
```

The `create` implementation is the same for `*List` kinds, except that each definition in the list will be created separately.

If the resource is namespaced (ie, not cluster-level), then one of `namespace`, `label_selector`, or `field_selector` is required.

If the resource is cluster-level, then one of `name`, `label_selector`, or `field_selector` is required.

## Delete

`delete(name=None, namespace=None, label_selector=None, field_selector=None, **kwargs)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

# Deletes the specific Service named 'example' from the 'test' namespace
v1_services.delete(name='my-service', namespace='test')

# Deletes all Services in the 'test' namespace
v1_services.delete(namespace='test')

# Deletes all Services in the 'test' namespace with the 'app' label set to 'foo'
v1_services.delete(namespace='test', label_selector='app=foo')

# Deletes all Services except for those in the 'default' namespace
v1_services.delete(field_selector='metadata.namespace!=default')
```

`delete(body=None, namespace=None, **kwargs)`

For List kind resources (ie, the resource name ends in `List`), the `delete` implementation is slightly different.
Rather than taking a name, they take a `*List` kind definition and call `delete` for each definition in the list.

```python
v1_service_list = dyn_client.resources.get(api_version='v1', kind='ServiceList')

body = {
    'kind': 'ServiceList',
    'apiVersion': 'v1',
    'items': [
        'metadata': {'name': 'my-service'},
        'spec': {
            'selector': {'app': 'MyApp'},
            'ports': [{
                'protocol': 'TCP',
                'port': '8080',
                'tardeletePort': '9376'
            }]
        }
    ],
    # More definitions would go here
}
# deletes the specified Service(s) from the 'test' namespace
v1_service_list.delete(body=body, namespace='test')

# Deletes all Services in the 'test' namespace
v1_service_list.delete(namespace='test')
```

## Patch

`patch(body=None, namespace=None, **kwargs)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

body = {
    'kind': 'Service',
    'apiVersion': 'v1',
    'metadata': {'name': 'my-service'},
    'spec': {
        'selector': {'app': 'MyApp2'},
    }
}

# patchs the above service in the 'test' namespace
v1_services.patch(body=body, namespace='test')
```

The `patch` implementation is the same for `*List` kinds, except that each definition in the list will be patched separately.

## Replace

`replace(body=None, namespace=None, **kwargs)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

body = {
    'kind': 'Service',
    'apiVersion': 'v1',
    'metadata': {'name': 'my-service'},
    'spec': {
        'selector': {'app': 'MyApp2'},
        'ports': [{
            'protocol': 'TCP',
            'port': '8080',
            'targetPort': '9376'
        }]
    }
}

# replaces the above service in the 'test' namespace
v1_services.replace(body=body, namespace='test')
```

The `replace` implementation is the same for `*List` kinds, except that each definition in the list will be replaced separately.

## Watch

`watch(namespace=None, name=None, label_selector=None, field_selector=None, resource_version=None, timeout=None)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

# Prints the resource that triggered each event related to Services in the 'test' namespace
for event in v1_services.watch(namespace='test'):
    print(event['object'])
```

# Community, Support, Discussion

If you have any problem with the package or any suggestions, please file an [issue](https://github.com/openshift/openshift-restclient-python/issues).

## Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).


