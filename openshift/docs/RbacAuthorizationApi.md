# openshift.openshift.client.RbacAuthorizationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_group**](RbacAuthorizationApi.md#get_api_group) | **GET** /apis/rbac.authorization.k8s.io/ | 


# **get_api_group**
> V1APIGroup get_api_group()



get information of a group

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
api_instance = openshift.openshift.client.RbacAuthorizationApi()

try: 
    api_response = api_instance.get_api_group()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RbacAuthorizationApi->get_api_group: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**V1APIGroup**](V1APIGroup.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json, application/yaml, application/vnd.kubernetes.protobuf
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

