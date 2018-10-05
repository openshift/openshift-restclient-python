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

From [PyPi](https://pypi.python.org/pypi/openshift/) directly:

```
pip install openshift
```

Using [Dockerfile](Dockerfile):

```
docker build -t openshift-restclient-python -f Dockerfile .
```

## Usage and examples

The OpenShift client depends on the [Kubernetes Python client](https://github.com/kubernetes-incubator/client-python.git), and as part of the installation process, the Kubernetes (K8s) client is automatically installed.

In the case you are using Docker, you will likely need to share your `.kube/config` with the `openshift-restclient-python` container:

```
docker run -it -v $HOME/.kube/config:/root/.kube/config:z openshift-restclient-python python
```

There are two ways this project interacts with the OpenShift API. The first, now deprecated, is to use models and functions generated with swagger from the API spec. The second, new approach, is
to use a single model and client to generically interact with all resources on the server. The dynamic client also works with
resources that are defined by aggregated API servers or Custom Resource Definitions.

### Dynamic client usage

To work with the dynamic client, you will need an instantiated kubernetes client object. For example, the following uses the dynamic client to create a new Service object:

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

Now in the following example, we use the dynamic client to create a Route object, and associate it with the new Service:

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

And finally, the following uses the dynamic client to list Projects the user can access:

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

#### Available methods for resources

The generic Resource class supports the following methods, though every resource kind does not support every method.


#### `get(name=None, namespace=None, label_selector=None, field_selector=None, **kwargs)`

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

#### `get(body=None, namespace=None, **kwargs)`

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

#### `create(body=None, namespace=None, **kwargs)`

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

#### `delete(name=None, namespace=None, label_selector=None, field_selector=None, **kwargs)`

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

#### `delete(body=None, namespace=None, **kwargs)`

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

#### `patch(body=None, namespace=None, **kwargs)`

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

#### `replace(body=None, namespace=None, **kwargs)`

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

#### `watch(namespace=None, name=None, label_selector=None, field_selector=None, resource_version=None, timeout=None)`

```python
v1_services = dyn_client.resources.get(api_version='v1', kind='Service')

# Prints the resource that triggered each event related to Services in the 'test' namespace
for event in v1_services.watch(namespace='test'):
    print(event['object'])
```

### DEPRECATED Generated client usage

To work with a K8s object, use the K8s client, and to work with an OpenShift specific object, use the OpenShift client. For example, the following uses the K8s client to create a new Service object:

```python
import yaml
from kubernetes import client, config

config.load_kube_config()
api = client.CoreV1Api()

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
resp = api.create_namespaced_service(body=service_data, namespace='default')

# resp is a V1Service object
print resp.metadata.self_link
```

Now in the following example, we use the OpenShift client to create a Route object, and associate it with the new Service:

```python
import yaml
from openshift import client, config

config.load_kube_config()
api = client.OapiApi()

route = """
apiVersion: v1
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
resp = api.create_namespaced_route(body=route_data, namespace='default')

# resp is a V1Route object
print resp.metadata.self_link
```

And finally, the following uses the OpenShift client to list Projects the user can access:

```python
from openshift import client, config

config.load_kube_config()
oapi = client.OapiApi()

project_list = oapi.list_project()
for project in project_list.items:
    print project.metadata.name
```

#### DEPRECATED Documentation

All OpenShift API and Model documentation can be found in the [Generated client's README file](openshift/README.md)

#### DEPRECATED  Update generated client

Updating the generated client requires the following tools:

- tox
- docker

To apply the updates:

1) Incorporate new changes to update scripts 
    - [scripts/constants.py](./scripts/constants.py), [scripts/pom.xml](./scripts/pom.xml), [scripts/preprocess_spec.py](./scripts/preprocess_spec.py), and [update-client.sh](./update-client.sh) are the most important
2) Run tox -e update_client

## Compatibility

We are downstream of the [kubernetes python client](github.com/kubernetes-client/python). We maintain compatibility for API version `n-2` - so if you are connecting to a version 3.6 OpenShift cluster, the list of supported python client versions would be `[0.3.x, 0.4.x, 0.5.x]`.

#### Compatibility matrix

| openshift python | kubernetes python | Kubernetes 1.5 | Kubernetes 1.6 | Kubernetes 1.7 | Kubernetes 1.8 | Kubernetes 1.9 |
|------------------|-------------------|----------------|----------------|----------------|----------------|----------------|
|  openshift 0.3   |  kubernetes 3.0   | +              | +              | ✓              | -              | -              |
|  openshift 0.4   |  kubernetes 4.0   | +*             | +              | +              | ✓              | -              |
|  openshift 0.5   |  kubernetes 5.0   | +*             | +*             | +              | +              | ✓              |
|  openshift HEAD  |  kubernetes HEAD  | +*             | +*             | +              | +              | ✓              |

Key:

* `✓` Exactly the same features / API objects in both openshift-restclient-python and the OpenShift
  version.
* `+` openshift-restclient-python has features or api objects that may not be present in the
  OpenShift cluster, but everything they have in common will work.
* `-` The OpenShift cluster has features the openshift-restclient-python library can't use
  (additional API objects, etc).
* `*` This client/server combination may work, but is not officially supported. 

## Community, Support, Discussion

If you have any problem with the package or any suggestions, please file an [issue](https://github.com/openshift/openshift-restclient-python/issues).

### Code of Conduct

Participation in the Kubernetes community is governed by the [CNCF Code of Conduct](https://github.com/cncf/foundation/blob/master/code-of-conduct.md).


