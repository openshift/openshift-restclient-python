# openshift.openshift.client.AuthenticationV1beta1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_review**](AuthenticationV1beta1Api.md#create_token_review) | **POST** /apis/authentication.k8s.io/v1beta1/tokenreviews | 
[**get_api_resources**](AuthenticationV1beta1Api.md#get_api_resources) | **GET** /apis/authentication.k8s.io/v1beta1/ | 


# **create_token_review**
> V1beta1TokenReview create_token_review(body, pretty=pretty)



create a TokenReview

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
api_instance = openshift.openshift.client.AuthenticationV1beta1Api()
body = openshift.openshift.client.V1beta1TokenReview() # V1beta1TokenReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_token_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationV1beta1Api->create_token_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1beta1TokenReview**](V1beta1TokenReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1beta1TokenReview**](V1beta1TokenReview.md)

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
api_instance = openshift.openshift.client.AuthenticationV1beta1Api()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationV1beta1Api->get_api_resources: %s\n" % e)
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

