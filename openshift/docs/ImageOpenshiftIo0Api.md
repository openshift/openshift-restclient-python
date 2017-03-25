# openshift.client.ImageOpenshiftIo0Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_openshift_io0_api_resources**](ImageOpenshiftIo0Api.md#get_image_openshift_io0_api_resources) | **GET** /apis/image.openshift.io/1.0/ | 


# **get_image_openshift_io0_api_resources**
> UnversionedAPIResourceList get_image_openshift_io0_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIo0Api()

try: 
    api_response = api_instance.get_image_openshift_io0_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIo0Api->get_image_openshift_io0_api_resources: %s\n" % e)
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

