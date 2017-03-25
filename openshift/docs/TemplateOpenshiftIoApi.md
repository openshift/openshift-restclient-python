# openshift.client.TemplateOpenshiftIoApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_namespaced_processed_template_v1**](TemplateOpenshiftIoApi.md#create_namespaced_processed_template_v1) | **POST** /apis/template.openshift.io/v1/namespaces/{namespace}/processedtemplates | 
[**create_processed_template_for_all_namespaces**](TemplateOpenshiftIoApi.md#create_processed_template_for_all_namespaces) | **POST** /apis/template.openshift.io/v1/processedtemplates | 


# **create_namespaced_processed_template_v1**
> V1Template create_namespaced_processed_template_v1(body, namespace, pretty=pretty)



create a Template

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.TemplateOpenshiftIoApi()
body = openshift.client.V1Template() # V1Template | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_processed_template_v1(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplateOpenshiftIoApi->create_namespaced_processed_template_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Template**](V1Template.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Template**](V1Template.md)

### Authorization

No authorization required

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
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.TemplateOpenshiftIoApi()
body = openshift.client.V1Template() # V1Template | 
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

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

