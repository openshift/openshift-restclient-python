# openshift.openshift.client.TemplateOpenshiftIoApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_processed_template_v1**](TemplateOpenshiftIoApi.md#create_namespaced_processed_template_v1) | **POST** /apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates | 
[**create_processed_template_for_all_namespaces**](TemplateOpenshiftIoApi.md#create_processed_template_for_all_namespaces) | **POST** /apis/template.openshift.io/v1/processedtemplates | 


# **create_namespaced_processed_template_v1**
> V1Template create_namespaced_processed_template_v1(namespace, body, pretty=pretty)



create a Template

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
api_instance = openshift.openshift.client.TemplateOpenshiftIoApi()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.openshift.client.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_processed_template_v1(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateOpenshiftIoApi->create_namespaced_processed_template_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1Template**](V1Template.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_processed_template_for_all_namespaces**
> V1Template create_processed_template_for_all_namespaces(body, pretty=pretty)



create a Template

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
api_instance = openshift.openshift.client.TemplateOpenshiftIoApi()
body = openshift.openshift.client.V1Template() # V1Template | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_processed_template_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateOpenshiftIoApi->create_processed_template_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

