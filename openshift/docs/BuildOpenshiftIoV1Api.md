# openshift.client.BuildOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary**](BuildOpenshiftIoV1Api.md#connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/instantiatebinary | 
[**connect_build_openshift_io_v1_post_namespaced_status_webhooks**](BuildOpenshiftIoV1Api.md#connect_build_openshift_io_v1_post_namespaced_status_webhooks) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks | 
[**connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path**](BuildOpenshiftIoV1Api.md#connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/webhooks/{path} | 
[**create_build_openshift_io_v1_build_config_for_all_namespaces**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_build_config_for_all_namespaces) | **POST** /apis/build.openshift.io/v1/buildconfigs | 
[**create_build_openshift_io_v1_build_for_all_namespaces**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_build_for_all_namespaces) | **POST** /apis/build.openshift.io/v1/builds | 
[**create_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_namespaced_build) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/builds | 
[**create_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_namespaced_build_config) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs | 
[**create_build_openshift_io_v1_namespaced_build_request_clone**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_namespaced_build_request_clone) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/clone | 
[**create_build_openshift_io_v1_namespaced_build_request_instantiate**](BuildOpenshiftIoV1Api.md#create_build_openshift_io_v1_namespaced_build_request_instantiate) | **POST** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name}/instantiate | 
[**delete_build_openshift_io_v1_collection_namespaced_build**](BuildOpenshiftIoV1Api.md#delete_build_openshift_io_v1_collection_namespaced_build) | **DELETE** /apis/build.openshift.io/v1/namespaces/{namespace}/builds | 
[**delete_build_openshift_io_v1_collection_namespaced_build_config**](BuildOpenshiftIoV1Api.md#delete_build_openshift_io_v1_collection_namespaced_build_config) | **DELETE** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs | 
[**delete_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#delete_build_openshift_io_v1_namespaced_build) | **DELETE** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name} | 
[**delete_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#delete_build_openshift_io_v1_namespaced_build_config) | **DELETE** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name} | 
[**get_build_openshift_io_v1_api_resources**](BuildOpenshiftIoV1Api.md#get_build_openshift_io_v1_api_resources) | **GET** /apis/build.openshift.io/v1/ | 
[**list_build_openshift_io_v1_build_config_for_all_namespaces**](BuildOpenshiftIoV1Api.md#list_build_openshift_io_v1_build_config_for_all_namespaces) | **GET** /apis/build.openshift.io/v1/buildconfigs | 
[**list_build_openshift_io_v1_build_for_all_namespaces**](BuildOpenshiftIoV1Api.md#list_build_openshift_io_v1_build_for_all_namespaces) | **GET** /apis/build.openshift.io/v1/builds | 
[**list_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#list_build_openshift_io_v1_namespaced_build) | **GET** /apis/build.openshift.io/v1/namespaces/{namespace}/builds | 
[**list_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#list_build_openshift_io_v1_namespaced_build_config) | **GET** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs | 
[**patch_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#patch_build_openshift_io_v1_namespaced_build) | **PATCH** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name} | 
[**patch_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#patch_build_openshift_io_v1_namespaced_build_config) | **PATCH** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name} | 
[**read_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#read_build_openshift_io_v1_namespaced_build) | **GET** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name} | 
[**read_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#read_build_openshift_io_v1_namespaced_build_config) | **GET** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name} | 
[**read_build_openshift_io_v1_namespaced_build_log_log**](BuildOpenshiftIoV1Api.md#read_build_openshift_io_v1_namespaced_build_log_log) | **GET** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/log | 
[**replace_build_openshift_io_v1_namespaced_build**](BuildOpenshiftIoV1Api.md#replace_build_openshift_io_v1_namespaced_build) | **PUT** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name} | 
[**replace_build_openshift_io_v1_namespaced_build_config**](BuildOpenshiftIoV1Api.md#replace_build_openshift_io_v1_namespaced_build_config) | **PUT** /apis/build.openshift.io/v1/namespaces/{namespace}/buildconfigs/{name} | 
[**replace_build_openshift_io_v1_namespaced_build_details**](BuildOpenshiftIoV1Api.md#replace_build_openshift_io_v1_namespaced_build_details) | **PUT** /apis/build.openshift.io/v1/namespaces/{namespace}/builds/{name}/details | 


# **connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary**
> str connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary(name, namespace, as_file=as_file, revision_author_email=revision_author_email, revision_author_name=revision_author_name, revision_commit=revision_commit, revision_committer_email=revision_committer_email, revision_committer_name=revision_committer_name, revision_message=revision_message)



connect POST requests to instantiatebinary of BinaryBuildRequestOptions

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BinaryBuildRequestOptions
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
as_file = 'as_file_example' # str | asFile determines if the binary should be created as a file within the source rather than extracted as an archive (optional)
revision_author_email = 'revision_author_email_example' # str | revision.authorEmail of the source control user (optional)
revision_author_name = 'revision_author_name_example' # str | revision.authorName of the source control user (optional)
revision_commit = 'revision_commit_example' # str | revision.commit is the value identifying a specific commit (optional)
revision_committer_email = 'revision_committer_email_example' # str | revision.committerEmail of the source control user (optional)
revision_committer_name = 'revision_committer_name_example' # str | revision.committerName of the source control user (optional)
revision_message = 'revision_message_example' # str | revision.message is the description of a specific commit (optional)

try: 
    api_response = api_instance.connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary(name, namespace, as_file=as_file, revision_author_email=revision_author_email, revision_author_name=revision_author_name, revision_commit=revision_commit, revision_committer_email=revision_committer_email, revision_committer_name=revision_committer_name, revision_message=revision_message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->connect_build_openshift_io_v1_post_namespaced_binary_build_request_options_instantiatebinary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BinaryBuildRequestOptions | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **as_file** | **str**| asFile determines if the binary should be created as a file within the source rather than extracted as an archive | [optional] 
 **revision_author_email** | **str**| revision.authorEmail of the source control user | [optional] 
 **revision_author_name** | **str**| revision.authorName of the source control user | [optional] 
 **revision_commit** | **str**| revision.commit is the value identifying a specific commit | [optional] 
 **revision_committer_email** | **str**| revision.committerEmail of the source control user | [optional] 
 **revision_committer_name** | **str**| revision.committerName of the source control user | [optional] 
 **revision_message** | **str**| revision.message is the description of a specific commit | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_build_openshift_io_v1_post_namespaced_status_webhooks**
> str connect_build_openshift_io_v1_post_namespaced_status_webhooks(name, namespace, path=path)



connect POST requests to webhooks of Status

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Status
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
path = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    api_response = api_instance.connect_build_openshift_io_v1_post_namespaced_status_webhooks(name, namespace, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->connect_build_openshift_io_v1_post_namespaced_status_webhooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Status | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **path** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path**
> str connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path(name, namespace, path, path2=path2)



connect POST requests to webhooks of Status

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Status
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
path = 'path_example' # str | path to the resource
path2 = 'path_example' # str | Path is the URL path to use for the current proxy request to pod. (optional)

try: 
    api_response = api_instance.connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path(name, namespace, path, path2=path2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->connect_build_openshift_io_v1_post_namespaced_status_webhooks_with_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Status | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **path** | **str**| path to the resource | 
 **path2** | **str**| Path is the URL path to use for the current proxy request to pod. | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_build_config_for_all_namespaces**
> V1BuildConfig create_build_openshift_io_v1_build_config_for_all_namespaces(body, pretty=pretty)



create a BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
body = openshift.client.V1BuildConfig() # V1BuildConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_build_config_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_build_config_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_build_for_all_namespaces**
> V1Build create_build_openshift_io_v1_build_for_all_namespaces(body, pretty=pretty)



create a Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
body = openshift.client.V1Build() # V1Build | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_build_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_build_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_namespaced_build**
> V1Build create_build_openshift_io_v1_namespaced_build(namespace, body, pretty=pretty)



create a Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1Build() # V1Build | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_namespaced_build(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_namespaced_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Build**](V1Build.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_namespaced_build_config**
> V1BuildConfig create_build_openshift_io_v1_namespaced_build_config(namespace, body, pretty=pretty)



create a BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1BuildConfig() # V1BuildConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_namespaced_build_config(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_namespaced_build_request_clone**
> V1BuildRequest create_build_openshift_io_v1_namespaced_build_request_clone(body, name, namespace, pretty=pretty)



create clone of a BuildRequest

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
body = openshift.client.V1BuildRequest() # V1BuildRequest | 
name = 'name_example' # str | name of the BuildRequest
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_namespaced_build_request_clone(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_namespaced_build_request_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildRequest**](V1BuildRequest.md)|  | 
 **name** | **str**| name of the BuildRequest | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildRequest**](V1BuildRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_build_openshift_io_v1_namespaced_build_request_instantiate**
> V1BuildRequest create_build_openshift_io_v1_namespaced_build_request_instantiate(body, name, namespace, pretty=pretty)



create instantiate of a BuildRequest

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
body = openshift.client.V1BuildRequest() # V1BuildRequest | 
name = 'name_example' # str | name of the BuildRequest
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_build_openshift_io_v1_namespaced_build_request_instantiate(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->create_build_openshift_io_v1_namespaced_build_request_instantiate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1BuildRequest**](V1BuildRequest.md)|  | 
 **name** | **str**| name of the BuildRequest | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildRequest**](V1BuildRequest.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_build_openshift_io_v1_collection_namespaced_build**
> UnversionedStatus delete_build_openshift_io_v1_collection_namespaced_build(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_build_openshift_io_v1_collection_namespaced_build(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->delete_build_openshift_io_v1_collection_namespaced_build: %s\n" % e)
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

# **delete_build_openshift_io_v1_collection_namespaced_build_config**
> UnversionedStatus delete_build_openshift_io_v1_collection_namespaced_build_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_build_openshift_io_v1_collection_namespaced_build_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->delete_build_openshift_io_v1_collection_namespaced_build_config: %s\n" % e)
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

# **delete_build_openshift_io_v1_namespaced_build**
> UnversionedStatus delete_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Build
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->delete_build_openshift_io_v1_namespaced_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Build | 
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

# **delete_build_openshift_io_v1_namespaced_build_config**
> UnversionedStatus delete_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete a BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BuildConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->delete_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BuildConfig | 
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

# **get_build_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_build_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_build_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->get_build_openshift_io_v1_api_resources: %s\n" % e)
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

# **list_build_openshift_io_v1_build_config_for_all_namespaces**
> V1BuildConfigList list_build_openshift_io_v1_build_config_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_build_openshift_io_v1_build_config_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->list_build_openshift_io_v1_build_config_for_all_namespaces: %s\n" % e)
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

[**V1BuildConfigList**](V1BuildConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_openshift_io_v1_build_for_all_namespaces**
> V1BuildList list_build_openshift_io_v1_build_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_build_openshift_io_v1_build_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->list_build_openshift_io_v1_build_for_all_namespaces: %s\n" % e)
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

[**V1BuildList**](V1BuildList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_openshift_io_v1_namespaced_build**
> V1BuildList list_build_openshift_io_v1_namespaced_build(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_build_openshift_io_v1_namespaced_build(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->list_build_openshift_io_v1_namespaced_build: %s\n" % e)
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

[**V1BuildList**](V1BuildList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_build_openshift_io_v1_namespaced_build_config**
> V1BuildConfigList list_build_openshift_io_v1_namespaced_build_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_build_openshift_io_v1_namespaced_build_config(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->list_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
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

[**V1BuildConfigList**](V1BuildConfigList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_build_openshift_io_v1_namespaced_build**
> V1Build patch_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty)



partially update the specified Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Build
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->patch_build_openshift_io_v1_namespaced_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Build | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_build_openshift_io_v1_namespaced_build_config**
> V1BuildConfig patch_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty)



partially update the specified BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BuildConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->patch_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BuildConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_build_openshift_io_v1_namespaced_build**
> V1Build read_build_openshift_io_v1_namespaced_build(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Build
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_build_openshift_io_v1_namespaced_build(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->read_build_openshift_io_v1_namespaced_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Build | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_build_openshift_io_v1_namespaced_build_config**
> V1BuildConfig read_build_openshift_io_v1_namespaced_build_config(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BuildConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_build_openshift_io_v1_namespaced_build_config(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->read_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BuildConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_build_openshift_io_v1_namespaced_build_log_log**
> V1BuildLog read_build_openshift_io_v1_namespaced_build_log_log(name, namespace, container=container, follow=follow, limit_bytes=limit_bytes, nowait=nowait, pretty=pretty, previous=previous, since_seconds=since_seconds, since_time=since_time, tail_lines=tail_lines, timestamps=timestamps, version=version)



read log of the specified BuildLog

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BuildLog
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
container = 'container_example' # str | cointainer for which to stream logs. Defaults to only container if there is one container in the pod. (optional)
follow = true # bool | follow if true indicates that the build log should be streamed until the build terminates. (optional)
limit_bytes = 56 # int | limitBytes, If set, is the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. (optional)
nowait = true # bool | noWait if true causes the call to return immediately even if the build is not available yet. Otherwise the server will wait until the build has started. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
previous = true # bool | previous returns previous build logs. Defaults to false. (optional)
since_seconds = 56 # int | sinceSeconds is a relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
since_time = 'since_time_example' # str | sinceTime is an RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. (optional)
tail_lines = 56 # int | tailLines, If set, is the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime (optional)
timestamps = true # bool | timestamps, If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. (optional)
version = 56 # int | version of the build for which to view logs. (optional)

try: 
    api_response = api_instance.read_build_openshift_io_v1_namespaced_build_log_log(name, namespace, container=container, follow=follow, limit_bytes=limit_bytes, nowait=nowait, pretty=pretty, previous=previous, since_seconds=since_seconds, since_time=since_time, tail_lines=tail_lines, timestamps=timestamps, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->read_build_openshift_io_v1_namespaced_build_log_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BuildLog | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **container** | **str**| cointainer for which to stream logs. Defaults to only container if there is one container in the pod. | [optional] 
 **follow** | **bool**| follow if true indicates that the build log should be streamed until the build terminates. | [optional] 
 **limit_bytes** | **int**| limitBytes, If set, is the number of bytes to read from the server before terminating the log output. This may not display a complete final line of logging, and may return slightly more or slightly less than the specified limit. | [optional] 
 **nowait** | **bool**| noWait if true causes the call to return immediately even if the build is not available yet. Otherwise the server will wait until the build has started. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **previous** | **bool**| previous returns previous build logs. Defaults to false. | [optional] 
 **since_seconds** | **int**| sinceSeconds is a relative time in seconds before the current time from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **since_time** | **str**| sinceTime is an RFC3339 timestamp from which to show logs. If this value precedes the time a pod was started, only logs since the pod start will be returned. If this value is in the future, no logs will be returned. Only one of sinceSeconds or sinceTime may be specified. | [optional] 
 **tail_lines** | **int**| tailLines, If set, is the number of lines from the end of the logs to show. If not specified, logs are shown from the creation of the container or sinceSeconds or sinceTime | [optional] 
 **timestamps** | **bool**| timestamps, If true, add an RFC3339 or RFC3339Nano timestamp at the beginning of every line of log output. Defaults to false. | [optional] 
 **version** | **int**| version of the build for which to view logs. | [optional] 

### Return type

[**V1BuildLog**](V1BuildLog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_build_openshift_io_v1_namespaced_build**
> V1Build replace_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty)



replace the specified Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the Build
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1Build() # V1Build | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_build_openshift_io_v1_namespaced_build(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->replace_build_openshift_io_v1_namespaced_build: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Build | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Build**](V1Build.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_build_openshift_io_v1_namespaced_build_config**
> V1BuildConfig replace_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty)



replace the specified BuildConfig

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
name = 'name_example' # str | name of the BuildConfig
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1BuildConfig() # V1BuildConfig | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_build_openshift_io_v1_namespaced_build_config(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->replace_build_openshift_io_v1_namespaced_build_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the BuildConfig | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1BuildConfig**](V1BuildConfig.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1BuildConfig**](V1BuildConfig.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_build_openshift_io_v1_namespaced_build_details**
> V1Build replace_build_openshift_io_v1_namespaced_build_details(body, name, namespace, pretty=pretty)



replace details of the specified Build

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.BuildOpenshiftIoV1Api()
body = openshift.client.V1Build() # V1Build | 
name = 'name_example' # str | name of the Build
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_build_openshift_io_v1_namespaced_build_details(body, name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BuildOpenshiftIoV1Api->replace_build_openshift_io_v1_namespaced_build_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Build**](V1Build.md)|  | 
 **name** | **str**| name of the Build | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Build**](V1Build.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

