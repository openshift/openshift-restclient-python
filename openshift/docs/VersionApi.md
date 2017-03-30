# openshift.client.VersionApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_code_version**](VersionApi.md#get_code_version) | **GET** /version/ | 


# **get_code_version**
> VersionInfo get_code_version()



get the code version

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.VersionApi()

try: 
    api_response = api_instance.get_code_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VersionApi->get_code_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionInfo**](VersionInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

