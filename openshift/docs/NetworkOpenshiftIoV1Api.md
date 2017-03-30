# openshift.client.NetworkOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#create_network_openshift_io_v1_cluster_network) | **POST** /apis/network.openshift.io/v1/clusternetworks | 
[**create_network_openshift_io_v1_egress_network_policy_for_all_namespaces**](NetworkOpenshiftIoV1Api.md#create_network_openshift_io_v1_egress_network_policy_for_all_namespaces) | **POST** /apis/network.openshift.io/v1/egressnetworkpolicies | 
[**create_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#create_network_openshift_io_v1_host_subnet) | **POST** /apis/network.openshift.io/v1/hostsubnets | 
[**create_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#create_network_openshift_io_v1_namespaced_egress_network_policy) | **POST** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies | 
[**create_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#create_network_openshift_io_v1_net_namespace) | **POST** /apis/network.openshift.io/v1/netnamespaces | 
[**delete_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_cluster_network) | **DELETE** /apis/network.openshift.io/v1/clusternetworks/{name} | 
[**delete_network_openshift_io_v1_collection_cluster_network**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_collection_cluster_network) | **DELETE** /apis/network.openshift.io/v1/clusternetworks | 
[**delete_network_openshift_io_v1_collection_host_subnet**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_collection_host_subnet) | **DELETE** /apis/network.openshift.io/v1/hostsubnets | 
[**delete_network_openshift_io_v1_collection_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_collection_namespaced_egress_network_policy) | **DELETE** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies | 
[**delete_network_openshift_io_v1_collection_net_namespace**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_collection_net_namespace) | **DELETE** /apis/network.openshift.io/v1/netnamespaces | 
[**delete_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_host_subnet) | **DELETE** /apis/network.openshift.io/v1/hostsubnets/{name} | 
[**delete_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_namespaced_egress_network_policy) | **DELETE** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies/{name} | 
[**delete_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#delete_network_openshift_io_v1_net_namespace) | **DELETE** /apis/network.openshift.io/v1/netnamespaces/{name} | 
[**get_network_openshift_io_v1_api_resources**](NetworkOpenshiftIoV1Api.md#get_network_openshift_io_v1_api_resources) | **GET** /apis/network.openshift.io/v1/ | 
[**list_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#list_network_openshift_io_v1_cluster_network) | **GET** /apis/network.openshift.io/v1/clusternetworks | 
[**list_network_openshift_io_v1_egress_network_policy_for_all_namespaces**](NetworkOpenshiftIoV1Api.md#list_network_openshift_io_v1_egress_network_policy_for_all_namespaces) | **GET** /apis/network.openshift.io/v1/egressnetworkpolicies | 
[**list_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#list_network_openshift_io_v1_host_subnet) | **GET** /apis/network.openshift.io/v1/hostsubnets | 
[**list_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#list_network_openshift_io_v1_namespaced_egress_network_policy) | **GET** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies | 
[**list_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#list_network_openshift_io_v1_net_namespace) | **GET** /apis/network.openshift.io/v1/netnamespaces | 
[**patch_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#patch_network_openshift_io_v1_cluster_network) | **PATCH** /apis/network.openshift.io/v1/clusternetworks/{name} | 
[**patch_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#patch_network_openshift_io_v1_host_subnet) | **PATCH** /apis/network.openshift.io/v1/hostsubnets/{name} | 
[**patch_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#patch_network_openshift_io_v1_namespaced_egress_network_policy) | **PATCH** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies/{name} | 
[**patch_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#patch_network_openshift_io_v1_net_namespace) | **PATCH** /apis/network.openshift.io/v1/netnamespaces/{name} | 
[**read_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#read_network_openshift_io_v1_cluster_network) | **GET** /apis/network.openshift.io/v1/clusternetworks/{name} | 
[**read_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#read_network_openshift_io_v1_host_subnet) | **GET** /apis/network.openshift.io/v1/hostsubnets/{name} | 
[**read_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#read_network_openshift_io_v1_namespaced_egress_network_policy) | **GET** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies/{name} | 
[**read_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#read_network_openshift_io_v1_net_namespace) | **GET** /apis/network.openshift.io/v1/netnamespaces/{name} | 
[**replace_network_openshift_io_v1_cluster_network**](NetworkOpenshiftIoV1Api.md#replace_network_openshift_io_v1_cluster_network) | **PUT** /apis/network.openshift.io/v1/clusternetworks/{name} | 
[**replace_network_openshift_io_v1_host_subnet**](NetworkOpenshiftIoV1Api.md#replace_network_openshift_io_v1_host_subnet) | **PUT** /apis/network.openshift.io/v1/hostsubnets/{name} | 
[**replace_network_openshift_io_v1_namespaced_egress_network_policy**](NetworkOpenshiftIoV1Api.md#replace_network_openshift_io_v1_namespaced_egress_network_policy) | **PUT** /apis/network.openshift.io/v1/namespaces/{namespace}/egressnetworkpolicies/{name} | 
[**replace_network_openshift_io_v1_net_namespace**](NetworkOpenshiftIoV1Api.md#replace_network_openshift_io_v1_net_namespace) | **PUT** /apis/network.openshift.io/v1/netnamespaces/{name} | 


# **create_network_openshift_io_v1_cluster_network**
> V1ClusterNetwork create_network_openshift_io_v1_cluster_network(body, pretty=pretty)



create a ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
body = openshift.client.V1ClusterNetwork() # V1ClusterNetwork | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_network_openshift_io_v1_cluster_network(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->create_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterNetwork**](V1ClusterNetwork.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_openshift_io_v1_egress_network_policy_for_all_namespaces**
> V1EgressNetworkPolicy create_network_openshift_io_v1_egress_network_policy_for_all_namespaces(body, pretty=pretty)



create an EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
body = openshift.client.V1EgressNetworkPolicy() # V1EgressNetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_network_openshift_io_v1_egress_network_policy_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->create_network_openshift_io_v1_egress_network_policy_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_openshift_io_v1_host_subnet**
> V1HostSubnet create_network_openshift_io_v1_host_subnet(body, pretty=pretty)



create a HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
body = openshift.client.V1HostSubnet() # V1HostSubnet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_network_openshift_io_v1_host_subnet(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->create_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1HostSubnet**](V1HostSubnet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_openshift_io_v1_namespaced_egress_network_policy**
> V1EgressNetworkPolicy create_network_openshift_io_v1_namespaced_egress_network_policy(namespace, body, pretty=pretty)



create an EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1EgressNetworkPolicy() # V1EgressNetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_network_openshift_io_v1_namespaced_egress_network_policy(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->create_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_openshift_io_v1_net_namespace**
> V1NetNamespace create_network_openshift_io_v1_net_namespace(body, pretty=pretty)



create a NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
body = openshift.client.V1NetNamespace() # V1NetNamespace | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_network_openshift_io_v1_net_namespace(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->create_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NetNamespace**](V1NetNamespace.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_cluster_network**
> UnversionedStatus delete_network_openshift_io_v1_cluster_network(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterNetwork
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_cluster_network(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_collection_cluster_network**
> UnversionedStatus delete_network_openshift_io_v1_collection_cluster_network(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_collection_cluster_network(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_collection_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_collection_host_subnet**
> UnversionedStatus delete_network_openshift_io_v1_collection_host_subnet(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_collection_host_subnet(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_collection_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_collection_namespaced_egress_network_policy**
> UnversionedStatus delete_network_openshift_io_v1_collection_namespaced_egress_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_collection_namespaced_egress_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_collection_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_collection_net_namespace**
> UnversionedStatus delete_network_openshift_io_v1_collection_net_namespace(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_collection_net_namespace(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_collection_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_host_subnet**
> UnversionedStatus delete_network_openshift_io_v1_host_subnet(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the HostSubnet
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_host_subnet(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_namespaced_egress_network_policy**
> UnversionedStatus delete_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete an EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the EgressNetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EgressNetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_openshift_io_v1_net_namespace**
> UnversionedStatus delete_network_openshift_io_v1_net_namespace(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the NetNamespace
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_network_openshift_io_v1_net_namespace(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->delete_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_network_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_network_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->get_network_openshift_io_v1_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIResourceList**](UnversionedAPIResourceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_openshift_io_v1_cluster_network**
> V1ClusterNetworkList list_network_openshift_io_v1_cluster_network(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_openshift_io_v1_cluster_network(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->list_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ClusterNetworkList**](V1ClusterNetworkList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_openshift_io_v1_egress_network_policy_for_all_namespaces**
> V1EgressNetworkPolicyList list_network_openshift_io_v1_egress_network_policy_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_openshift_io_v1_egress_network_policy_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->list_network_openshift_io_v1_egress_network_policy_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1EgressNetworkPolicyList**](V1EgressNetworkPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_openshift_io_v1_host_subnet**
> V1HostSubnetList list_network_openshift_io_v1_host_subnet(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_openshift_io_v1_host_subnet(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->list_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1HostSubnetList**](V1HostSubnetList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_openshift_io_v1_namespaced_egress_network_policy**
> V1EgressNetworkPolicyList list_network_openshift_io_v1_namespaced_egress_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_openshift_io_v1_namespaced_egress_network_policy(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->list_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1EgressNetworkPolicyList**](V1EgressNetworkPolicyList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_openshift_io_v1_net_namespace**
> V1NetNamespaceList list_network_openshift_io_v1_net_namespace(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_network_openshift_io_v1_net_namespace(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->list_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1NetNamespaceList**](V1NetNamespaceList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_openshift_io_v1_cluster_network**
> V1ClusterNetwork patch_network_openshift_io_v1_cluster_network(name, body, pretty=pretty)



partially update the specified ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterNetwork
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_network_openshift_io_v1_cluster_network(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->patch_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_openshift_io_v1_host_subnet**
> V1HostSubnet patch_network_openshift_io_v1_host_subnet(name, body, pretty=pretty)



partially update the specified HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the HostSubnet
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_network_openshift_io_v1_host_subnet(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->patch_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_openshift_io_v1_namespaced_egress_network_policy**
> V1EgressNetworkPolicy patch_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty)



partially update the specified EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the EgressNetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->patch_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EgressNetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network_openshift_io_v1_net_namespace**
> V1NetNamespace patch_network_openshift_io_v1_net_namespace(name, body, pretty=pretty)



partially update the specified NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the NetNamespace
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_network_openshift_io_v1_net_namespace(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->patch_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_openshift_io_v1_cluster_network**
> V1ClusterNetwork read_network_openshift_io_v1_cluster_network(name, pretty=pretty, exact=exact, export=export)



read the specified ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterNetwork
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_network_openshift_io_v1_cluster_network(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->read_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_openshift_io_v1_host_subnet**
> V1HostSubnet read_network_openshift_io_v1_host_subnet(name, pretty=pretty, exact=exact, export=export)



read the specified HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the HostSubnet
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_network_openshift_io_v1_host_subnet(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->read_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_openshift_io_v1_namespaced_egress_network_policy**
> V1EgressNetworkPolicy read_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the EgressNetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->read_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EgressNetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_network_openshift_io_v1_net_namespace**
> V1NetNamespace read_network_openshift_io_v1_net_namespace(name, pretty=pretty, exact=exact, export=export)



read the specified NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the NetNamespace
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_network_openshift_io_v1_net_namespace(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->read_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_network_openshift_io_v1_cluster_network**
> V1ClusterNetwork replace_network_openshift_io_v1_cluster_network(name, body, pretty=pretty)



replace the specified ClusterNetwork

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterNetwork
body = openshift.client.V1ClusterNetwork() # V1ClusterNetwork | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_network_openshift_io_v1_cluster_network(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->replace_network_openshift_io_v1_cluster_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterNetwork | 
 **body** | [**V1ClusterNetwork**](V1ClusterNetwork.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterNetwork**](V1ClusterNetwork.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_network_openshift_io_v1_host_subnet**
> V1HostSubnet replace_network_openshift_io_v1_host_subnet(name, body, pretty=pretty)



replace the specified HostSubnet

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the HostSubnet
body = openshift.client.V1HostSubnet() # V1HostSubnet | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_network_openshift_io_v1_host_subnet(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->replace_network_openshift_io_v1_host_subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the HostSubnet | 
 **body** | [**V1HostSubnet**](V1HostSubnet.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1HostSubnet**](V1HostSubnet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_network_openshift_io_v1_namespaced_egress_network_policy**
> V1EgressNetworkPolicy replace_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty)



replace the specified EgressNetworkPolicy

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the EgressNetworkPolicy
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1EgressNetworkPolicy() # V1EgressNetworkPolicy | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_network_openshift_io_v1_namespaced_egress_network_policy(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->replace_network_openshift_io_v1_namespaced_egress_network_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the EgressNetworkPolicy | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1EgressNetworkPolicy**](V1EgressNetworkPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_network_openshift_io_v1_net_namespace**
> V1NetNamespace replace_network_openshift_io_v1_net_namespace(name, body, pretty=pretty)



replace the specified NetNamespace

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.NetworkOpenshiftIoV1Api()
name = 'name_example' # str | name of the NetNamespace
body = openshift.client.V1NetNamespace() # V1NetNamespace | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_network_openshift_io_v1_net_namespace(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NetworkOpenshiftIoV1Api->replace_network_openshift_io_v1_net_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the NetNamespace | 
 **body** | [**V1NetNamespace**](V1NetNamespace.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1NetNamespace**](V1NetNamespace.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

