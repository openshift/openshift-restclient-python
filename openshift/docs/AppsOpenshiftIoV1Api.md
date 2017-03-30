# openshift.client.AppsOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apps_openshift_io_v1_deployment_config_for_all_namespaces**](AppsOpenshiftIoV1Api.md#create_apps_openshift_io_v1_deployment_config_for_all_namespaces) | **POST** /apis/apps.openshift.io/v1/deploymentconfigs | 
[**create_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#create_apps_openshift_io_v1_namespaced_deployment_config) | **POST** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs | 
[**create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback**](AppsOpenshiftIoV1Api.md#create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback) | **POST** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/rollback | 
[**create_apps_openshift_io_v1_namespaced_deployment_request_instantiate**](AppsOpenshiftIoV1Api.md#create_apps_openshift_io_v1_namespaced_deployment_request_instantiate) | **POST** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/instantiate | 
[**delete_apps_openshift_io_v1_collection_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#delete_apps_openshift_io_v1_collection_namespaced_deployment_config) | **DELETE** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs | 
[**delete_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#delete_apps_openshift_io_v1_namespaced_deployment_config) | **DELETE** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name} | 
[**get_apps_openshift_io_v1_api_resources**](AppsOpenshiftIoV1Api.md#get_apps_openshift_io_v1_api_resources) | **GET** /apis/apps.openshift.io/v1/ | 
[**list_apps_openshift_io_v1_deployment_config_for_all_namespaces**](AppsOpenshiftIoV1Api.md#list_apps_openshift_io_v1_deployment_config_for_all_namespaces) | **GET** /apis/apps.openshift.io/v1/deploymentconfigs | 
[**list_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#list_apps_openshift_io_v1_namespaced_deployment_config) | **GET** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs | 
[**patch_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#patch_apps_openshift_io_v1_namespaced_deployment_config) | **PATCH** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name} | 
[**patch_apps_openshift_io_v1_namespaced_deployment_config_status**](AppsOpenshiftIoV1Api.md#patch_apps_openshift_io_v1_namespaced_deployment_config_status) | **PATCH** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/status | 
[**patch_apps_openshift_io_v1_namespaced_scale_scale**](AppsOpenshiftIoV1Api.md#patch_apps_openshift_io_v1_namespaced_scale_scale) | **PATCH** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | 
[**read_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#read_apps_openshift_io_v1_namespaced_deployment_config) | **GET** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name} | 
[**read_apps_openshift_io_v1_namespaced_deployment_config_status**](AppsOpenshiftIoV1Api.md#read_apps_openshift_io_v1_namespaced_deployment_config_status) | **GET** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/status | 
[**read_apps_openshift_io_v1_namespaced_deployment_log_log**](AppsOpenshiftIoV1Api.md#read_apps_openshift_io_v1_namespaced_deployment_log_log) | **GET** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/log | 
[**read_apps_openshift_io_v1_namespaced_scale_scale**](AppsOpenshiftIoV1Api.md#read_apps_openshift_io_v1_namespaced_scale_scale) | **GET** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | 
[**replace_apps_openshift_io_v1_namespaced_deployment_config**](AppsOpenshiftIoV1Api.md#replace_apps_openshift_io_v1_namespaced_deployment_config) | **PUT** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name} | 
[**replace_apps_openshift_io_v1_namespaced_deployment_config_status**](AppsOpenshiftIoV1Api.md#replace_apps_openshift_io_v1_namespaced_deployment_config_status) | **PUT** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/status | 
[**replace_apps_openshift_io_v1_namespaced_scale_scale**](AppsOpenshiftIoV1Api.md#replace_apps_openshift_io_v1_namespaced_scale_scale) | **PUT** /apis/apps.openshift.io/v1/namespaces/{namespace}/deploymentconfigs/{name}/scale | 


# **create_apps_openshift_io_v1_deployment_config_for_all_namespaces**
> V1DeploymentConfig create_apps_openshift_io_v1_deployment_config_for_all_namespaces(body, pretty=pretty)



create a DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
body = openshift.client.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_apps_openshift_io_v1_deployment_config_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->create_apps_openshift_io_v1_deployment_config_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_apps_openshift_io_v1_namespaced_deployment_config**
> V1DeploymentConfig create_apps_openshift_io_v1_namespaced_deployment_config(namespace, body, pretty=pretty)



create a DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_apps_openshift_io_v1_namespaced_deployment_config(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->create_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback**
> V1DeploymentConfigRollback create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback(body, name, namespace, pretty=pretty)



create rollback of a DeploymentConfigRollback

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
body = openshift.client.V1DeploymentConfigRollback() # V1DeploymentConfigRollback | 
name = 'name_example' # str | name of the DeploymentConfigRollback
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->create_apps_openshift_io_v1_namespaced_deployment_config_rollback_rollback: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)|  | 
 **name** | **str**| name of the DeploymentConfigRollback | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfigRollback**](V1DeploymentConfigRollback.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_apps_openshift_io_v1_namespaced_deployment_request_instantiate**
> V1DeploymentRequest create_apps_openshift_io_v1_namespaced_deployment_request_instantiate(body, name, namespace, pretty=pretty)



create instantiate of a DeploymentRequest

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
body = openshift.client.V1DeploymentRequest() # V1DeploymentRequest | 
name = 'name_example' # str | name of the DeploymentRequest
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_apps_openshift_io_v1_namespaced_deployment_request_instantiate(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->create_apps_openshift_io_v1_namespaced_deployment_request_instantiate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1DeploymentRequest**](V1DeploymentRequest.md)|  | 
 **name** | **str**| name of the DeploymentRequest | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentRequest**](V1DeploymentRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_apps_openshift_io_v1_collection_namespaced_deployment_config**
> UnversionedStatus delete_apps_openshift_io_v1_collection_namespaced_deployment_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_apps_openshift_io_v1_collection_namespaced_deployment_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->delete_apps_openshift_io_v1_collection_namespaced_deployment_config: %s\n" % e)
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

# **delete_apps_openshift_io_v1_namespaced_deployment_config**
> UnversionedStatus delete_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->delete_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
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

# **get_apps_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_apps_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_apps_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->get_apps_openshift_io_v1_api_resources: %s\n" % e)
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

# **list_apps_openshift_io_v1_deployment_config_for_all_namespaces**
> V1DeploymentConfigList list_apps_openshift_io_v1_deployment_config_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_apps_openshift_io_v1_deployment_config_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->list_apps_openshift_io_v1_deployment_config_for_all_namespaces: %s\n" % e)
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

[**V1DeploymentConfigList**](V1DeploymentConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps_openshift_io_v1_namespaced_deployment_config**
> V1DeploymentConfigList list_apps_openshift_io_v1_namespaced_deployment_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_apps_openshift_io_v1_namespaced_deployment_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->list_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
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

[**V1DeploymentConfigList**](V1DeploymentConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_apps_openshift_io_v1_namespaced_deployment_config**
> V1DeploymentConfig patch_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty)



partially update the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->patch_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_apps_openshift_io_v1_namespaced_deployment_config_status**
> V1DeploymentConfig patch_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, body, pretty=pretty)



partially update status of the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->patch_apps_openshift_io_v1_namespaced_deployment_config_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_apps_openshift_io_v1_namespaced_scale_scale**
> V1beta1Scale patch_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, body, pretty=pretty)



partially update scale of the specified Scale

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->patch_apps_openshift_io_v1_namespaced_scale_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_apps_openshift_io_v1_namespaced_deployment_config**
> V1DeploymentConfig read_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->read_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_apps_openshift_io_v1_namespaced_deployment_config_status**
> V1DeploymentConfig read_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, pretty=pretty)



read status of the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->read_apps_openshift_io_v1_namespaced_deployment_config_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_apps_openshift_io_v1_namespaced_deployment_log_log**
> V1DeploymentLog read_apps_openshift_io_v1_namespaced_deployment_log_log(name, namespace, container=container, follow=follow, limit_bytes=limit_bytes, nowait=nowait, pretty=pretty, previous=previous, since_seconds=since_seconds, since_time=since_time, tail_lines=tail_lines, timestamps=timestamps, version=version)



read log of the specified DeploymentLog

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentLog
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
container = 'container_example' # str | The container for which to stream logs. Defaults to only container if there is one container in the pod. (optional)
follow = true # bool | Follow if true indicates that the build log should be streamed until the build terminates. (optional)
limit_bytes = 56 # int | If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. (optional)
nowait = true # bool | NoWait if true causes the call to return immediately even if the deployment is not available yet. Otherwise the server will wait until the deployment has started. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
previous = true # bool | Return previous deployment logs. Defaults to false. (optional)
since_seconds = 56 # int | A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
since_time = 'since_time_example' # str | An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
tail_lines = 56 # int | If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime (optional)
timestamps = true # bool | If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. (optional)
version = 56 # int | Version of the deployment for which to view logs. (optional)

try: 
    api_response = api_instance.read_apps_openshift_io_v1_namespaced_deployment_log_log(name, namespace, container=container, follow=follow, limit_bytes=limit_bytes, nowait=nowait, pretty=pretty, previous=previous, since_seconds=since_seconds, since_time=since_time, tail_lines=tail_lines, timestamps=timestamps, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->read_apps_openshift_io_v1_namespaced_deployment_log_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentLog | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **container** | **str**| The container for which to stream logs. Defaults to only container if there is one container in the pod. | [optional] 
 **follow** | **bool**| Follow if true indicates that the build log should be streamed until the build terminates. | [optional] 
 **limit_bytes** | **int**| If set, the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. | [optional] 
 **nowait** | **bool**| NoWait if true causes the call to return immediately even if the deployment is not available yet. Otherwise the server will wait until the deployment has started. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **previous** | **bool**| Return previous deployment logs. Defaults to false. | [optional] 
 **since_seconds** | **int**| A relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **since_time** | **str**| An RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **tail_lines** | **int**| If set, the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime | [optional] 
 **timestamps** | **bool**| If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. | [optional] 
 **version** | **int**| Version of the deployment for which to view logs. | [optional] 

### Return type

[**V1DeploymentLog**](V1DeploymentLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_apps_openshift_io_v1_namespaced_scale_scale**
> V1beta1Scale read_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, pretty=pretty)



read scale of the specified Scale

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->read_apps_openshift_io_v1_namespaced_scale_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_apps_openshift_io_v1_namespaced_deployment_config**
> V1DeploymentConfig replace_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty)



replace the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_apps_openshift_io_v1_namespaced_deployment_config(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->replace_apps_openshift_io_v1_namespaced_deployment_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_apps_openshift_io_v1_namespaced_deployment_config_status**
> V1DeploymentConfig replace_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, body, pretty=pretty)



replace status of the specified DeploymentConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the DeploymentConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeploymentConfig() # V1DeploymentConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_apps_openshift_io_v1_namespaced_deployment_config_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->replace_apps_openshift_io_v1_namespaced_deployment_config_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the DeploymentConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeploymentConfig**](V1DeploymentConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1DeploymentConfig**](V1DeploymentConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_apps_openshift_io_v1_namespaced_scale_scale**
> V1beta1Scale replace_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, body, pretty=pretty)



replace scale of the specified Scale

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.AppsOpenshiftIoV1Api()
name = 'name_example' # str | name of the Scale
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1beta1Scale() # V1beta1Scale | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_apps_openshift_io_v1_namespaced_scale_scale(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsOpenshiftIoV1Api->replace_apps_openshift_io_v1_namespaced_scale_scale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Scale | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1beta1Scale**](V1beta1Scale.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1Scale**](V1beta1Scale.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

