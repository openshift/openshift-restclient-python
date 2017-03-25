# openshift.client.SecurityOpenshiftIoApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security_openshift_io_api_group**](SecurityOpenshiftIoApi.md#get_security_openshift_io_api_group) | **GET** /apis/security.openshift.io/ | 


# **get_security_openshift_io_api_group**
> UnversionedAPIGroup get_security_openshift_io_api_group()



get information of a group

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoApi()

try: 
    api_response = api_instance.get_security_openshift_io_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoApi->get_security_openshift_io_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnversionedAPIGroup**](UnversionedAPIGroup.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

