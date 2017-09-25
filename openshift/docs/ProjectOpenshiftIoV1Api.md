# openshift.openshift.client.ProjectOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectOpenshiftIoV1Api.md#create_project) | **POST** /apis/project.openshift.io/v1/projects | 
[**create_project_request**](ProjectOpenshiftIoV1Api.md#create_project_request) | **POST** /apis/project.openshift.io/v1/projectrequests | 
[**delete_project**](ProjectOpenshiftIoV1Api.md#delete_project) | **DELETE** /apis/project.openshift.io/v1/projects/{name} | 
[**get_api_resources**](ProjectOpenshiftIoV1Api.md#get_api_resources) | **GET** /apis/project.openshift.io/v1/ | 
[**list_project**](ProjectOpenshiftIoV1Api.md#list_project) | **GET** /apis/project.openshift.io/v1/projects | 
[**list_project_request**](ProjectOpenshiftIoV1Api.md#list_project_request) | **GET** /apis/project.openshift.io/v1/projectrequests | 
[**patch_project**](ProjectOpenshiftIoV1Api.md#patch_project) | **PATCH** /apis/project.openshift.io/v1/projects/{name} | 
[**read_project**](ProjectOpenshiftIoV1Api.md#read_project) | **GET** /apis/project.openshift.io/v1/projects/{name} | 
[**replace_project**](ProjectOpenshiftIoV1Api.md#replace_project) | **PUT** /apis/project.openshift.io/v1/projects/{name} | 


# **create_project**
> V1Project create_project(body, pretty=pretty)



create a Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
body = openshift.openshift.client.V1Project() # V1Project | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_project(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Project**](V1Project.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project_request**
> V1ProjectRequest create_project_request(body, pretty=pretty)



create a ProjectRequest

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
body = openshift.openshift.client.V1ProjectRequest() # V1ProjectRequest | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_project_request(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->create_project_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ProjectRequest**](V1ProjectRequest.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ProjectRequest**](V1ProjectRequest.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> V1Status delete_project(name, pretty=pretty)



delete a Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_resources**
> V1APIResourceList get_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->get_api_resources: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIResourceList**](V1APIResourceList.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project**
> V1ProjectList list_project(pretty=pretty, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_project(pretty=pretty, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->list_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ProjectList**](V1ProjectList.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_request**
> V1Status list_project_request(pretty=pretty, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list objects of kind ProjectRequest

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
include_uninitialized = true # bool | If true, partially initialized resources are included in the response. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it's 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_project_request(pretty=pretty, field_selector=field_selector, include_uninitialized=include_uninitialized, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->list_project_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **include_uninitialized** | **bool**| If true, partially initialized resources are included in the response. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. When specified for list: - if unset, then the result is returned from remote storage based on quorum-read flag; - if it&#39;s 0, then we simply return what we currently have in cache, no guarantee; - if set to non zero, then the result is at least as fresh as given rv. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1Status**](V1Status.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_project**
> V1Project patch_project(name, body, pretty=pretty)



partially update the specified Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
name = 'name_example' # str | name of the Project
body = NULL # object | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_project(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->patch_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **body** | **object**|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_project**
> V1Project read_project(name, pretty=pretty)



read the specified Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
name = 'name_example' # str | name of the Project
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_project(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->read_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_project**
> V1Project replace_project(name, body, pretty=pretty)



replace the specified Project

### Example 
```python
from __future__ import print_statement
import time
import openshift.openshift.client
from openshift.openshift.client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: Oauth2Implicit
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: Oauth2AccessToken
openshift.openshift.client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure API key authorization: BearerToken
openshift.openshift.client.configuration.api_key['authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# openshift.openshift.client.configuration.api_key_prefix['authorization'] = 'Bearer'

# create an instance of the API class
api_instance = openshift.openshift.client.ProjectOpenshiftIoV1Api()
name = 'name_example' # str | name of the Project
body = openshift.openshift.client.V1Project() # V1Project | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_project(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectOpenshiftIoV1Api->replace_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Project | 
 **body** | [**V1Project**](V1Project.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Project**](V1Project.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

