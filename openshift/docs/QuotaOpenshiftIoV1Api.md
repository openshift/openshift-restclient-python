# openshift.client.QuotaOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#create_quota_openshift_io_v1_cluster_resource_quota) | **POST** /apis/quota.openshift.io/v1/clusterresourcequotas | 
[**delete_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#delete_quota_openshift_io_v1_cluster_resource_quota) | **DELETE** /apis/quota.openshift.io/v1/clusterresourcequotas/{name} | 
[**delete_quota_openshift_io_v1_collection_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#delete_quota_openshift_io_v1_collection_cluster_resource_quota) | **DELETE** /apis/quota.openshift.io/v1/clusterresourcequotas | 
[**get_quota_openshift_io_v1_api_resources**](QuotaOpenshiftIoV1Api.md#get_quota_openshift_io_v1_api_resources) | **GET** /apis/quota.openshift.io/v1/ | 
[**list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces**](QuotaOpenshiftIoV1Api.md#list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces) | **GET** /apis/quota.openshift.io/v1/appliedclusterresourcequotas | 
[**list_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#list_quota_openshift_io_v1_cluster_resource_quota) | **GET** /apis/quota.openshift.io/v1/clusterresourcequotas | 
[**list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota) | **GET** /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas | 
[**patch_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#patch_quota_openshift_io_v1_cluster_resource_quota) | **PATCH** /apis/quota.openshift.io/v1/clusterresourcequotas/{name} | 
[**patch_quota_openshift_io_v1_cluster_resource_quota_status**](QuotaOpenshiftIoV1Api.md#patch_quota_openshift_io_v1_cluster_resource_quota_status) | **PATCH** /apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status | 
[**read_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#read_quota_openshift_io_v1_cluster_resource_quota) | **GET** /apis/quota.openshift.io/v1/clusterresourcequotas/{name} | 
[**read_quota_openshift_io_v1_cluster_resource_quota_status**](QuotaOpenshiftIoV1Api.md#read_quota_openshift_io_v1_cluster_resource_quota_status) | **GET** /apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status | 
[**read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota) | **GET** /apis/quota.openshift.io/v1/namespaces/{namespace}/appliedclusterresourcequotas/{name} | 
[**replace_quota_openshift_io_v1_cluster_resource_quota**](QuotaOpenshiftIoV1Api.md#replace_quota_openshift_io_v1_cluster_resource_quota) | **PUT** /apis/quota.openshift.io/v1/clusterresourcequotas/{name} | 
[**replace_quota_openshift_io_v1_cluster_resource_quota_status**](QuotaOpenshiftIoV1Api.md#replace_quota_openshift_io_v1_cluster_resource_quota_status) | **PUT** /apis/quota.openshift.io/v1/clusterresourcequotas/{name}/status | 


# **create_quota_openshift_io_v1_cluster_resource_quota**
> V1ClusterResourceQuota create_quota_openshift_io_v1_cluster_resource_quota(body, pretty=pretty)



create a ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
body = openshift.client.V1ClusterResourceQuota() # V1ClusterResourceQuota | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_quota_openshift_io_v1_cluster_resource_quota(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->create_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_quota_openshift_io_v1_cluster_resource_quota**
> UnversionedStatus delete_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->delete_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
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

# **delete_quota_openshift_io_v1_collection_cluster_resource_quota**
> UnversionedStatus delete_quota_openshift_io_v1_collection_cluster_resource_quota(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_quota_openshift_io_v1_collection_cluster_resource_quota(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->delete_quota_openshift_io_v1_collection_cluster_resource_quota: %s\n" % e)
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

# **get_quota_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_quota_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_quota_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->get_quota_openshift_io_v1_api_resources: %s\n" % e)
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

# **list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces**
> V1AppliedClusterResourceQuotaList list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list objects of kind AppliedClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces(field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->list_quota_openshift_io_v1_applied_cluster_resource_quota_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1AppliedClusterResourceQuotaList**](V1AppliedClusterResourceQuotaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_openshift_io_v1_cluster_resource_quota**
> V1ClusterResourceQuotaList list_quota_openshift_io_v1_cluster_resource_quota(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_quota_openshift_io_v1_cluster_resource_quota(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->list_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
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

[**V1ClusterResourceQuotaList**](V1ClusterResourceQuotaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota**
> V1AppliedClusterResourceQuotaList list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list objects of kind AppliedClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota(namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->list_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1AppliedClusterResourceQuotaList**](V1AppliedClusterResourceQuotaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_quota_openshift_io_v1_cluster_resource_quota**
> V1ClusterResourceQuota patch_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty)



partially update the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->patch_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_quota_openshift_io_v1_cluster_resource_quota_status**
> V1ClusterResourceQuota patch_quota_openshift_io_v1_cluster_resource_quota_status(name, body, pretty=pretty)



partially update status of the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_quota_openshift_io_v1_cluster_resource_quota_status(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->patch_quota_openshift_io_v1_cluster_resource_quota_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_quota_openshift_io_v1_cluster_resource_quota**
> V1ClusterResourceQuota read_quota_openshift_io_v1_cluster_resource_quota(name, pretty=pretty, exact=exact, export=export)



read the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_quota_openshift_io_v1_cluster_resource_quota(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->read_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_quota_openshift_io_v1_cluster_resource_quota_status**
> V1ClusterResourceQuota read_quota_openshift_io_v1_cluster_resource_quota_status(name, pretty=pretty)



read status of the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_quota_openshift_io_v1_cluster_resource_quota_status(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->read_quota_openshift_io_v1_cluster_resource_quota_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota**
> V1AppliedClusterResourceQuota read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota(name, namespace, pretty=pretty)



read the specified AppliedClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the AppliedClusterResourceQuota
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->read_quota_openshift_io_v1_namespaced_applied_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the AppliedClusterResourceQuota | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1AppliedClusterResourceQuota**](V1AppliedClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_quota_openshift_io_v1_cluster_resource_quota**
> V1ClusterResourceQuota replace_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty)



replace the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
body = openshift.client.V1ClusterResourceQuota() # V1ClusterResourceQuota | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_quota_openshift_io_v1_cluster_resource_quota(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->replace_quota_openshift_io_v1_cluster_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **body** | [**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_quota_openshift_io_v1_cluster_resource_quota_status**
> V1ClusterResourceQuota replace_quota_openshift_io_v1_cluster_resource_quota_status(name, body, pretty=pretty)



replace status of the specified ClusterResourceQuota

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.QuotaOpenshiftIoV1Api()
name = 'name_example' # str | name of the ClusterResourceQuota
body = openshift.client.V1ClusterResourceQuota() # V1ClusterResourceQuota | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_quota_openshift_io_v1_cluster_resource_quota_status(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotaOpenshiftIoV1Api->replace_quota_openshift_io_v1_cluster_resource_quota_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ClusterResourceQuota | 
 **body** | [**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ClusterResourceQuota**](V1ClusterResourceQuota.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

