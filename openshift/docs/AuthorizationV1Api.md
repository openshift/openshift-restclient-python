# openshift.openshift.client.AuthorizationV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_local_subject_access_review_for_all_namespaces**](AuthorizationV1Api.md#create_local_subject_access_review_for_all_namespaces) | **POST** /apis/authorization.k8s.io/v1/localsubjectaccessreviews | 
[**create_namespaced_local_subject_access_review**](AuthorizationV1Api.md#create_namespaced_local_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/namespaces/{namespace}/localsubjectaccessreviews | 
[**create_self_subject_access_review**](AuthorizationV1Api.md#create_self_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/selfsubjectaccessreviews | 
[**create_subject_access_review**](AuthorizationV1Api.md#create_subject_access_review) | **POST** /apis/authorization.k8s.io/v1/subjectaccessreviews | 
[**get_api_resources**](AuthorizationV1Api.md#get_api_resources) | **GET** /apis/authorization.k8s.io/v1/ | 


# **create_local_subject_access_review_for_all_namespaces**
> V1LocalSubjectAccessReview create_local_subject_access_review_for_all_namespaces(body, pretty=pretty)



create a LocalSubjectAccessReview

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
api_instance = openshift.openshift.client.AuthorizationV1Api()
body = openshift.openshift.client.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_local_subject_access_review_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_local_subject_access_review_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_namespaced_local_subject_access_review**
> V1LocalSubjectAccessReview create_namespaced_local_subject_access_review(namespace, body, pretty=pretty)



create a LocalSubjectAccessReview

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
api_instance = openshift.openshift.client.AuthorizationV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.openshift.client.V1LocalSubjectAccessReview() # V1LocalSubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_namespaced_local_subject_access_review(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_namespaced_local_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1LocalSubjectAccessReview**](V1LocalSubjectAccessReview.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_self_subject_access_review**
> V1SelfSubjectAccessReview create_self_subject_access_review(body, pretty=pretty)



create a SelfSubjectAccessReview

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
api_instance = openshift.openshift.client.AuthorizationV1Api()
body = openshift.openshift.client.V1SelfSubjectAccessReview() # V1SelfSubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_self_subject_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_self_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SelfSubjectAccessReview**](V1SelfSubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SelfSubjectAccessReview**](V1SelfSubjectAccessReview.md)

### Authorization

[Oauth2Implicit](../README.md#Oauth2Implicit), [Oauth2AccessToken](../README.md#Oauth2AccessToken), [BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_subject_access_review**
> V1SubjectAccessReview create_subject_access_review(body, pretty=pretty)



create a SubjectAccessReview

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
api_instance = openshift.openshift.client.AuthorizationV1Api()
body = openshift.openshift.client.V1SubjectAccessReview() # V1SubjectAccessReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_subject_access_review(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->create_subject_access_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1SubjectAccessReview**](V1SubjectAccessReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1SubjectAccessReview**](V1SubjectAccessReview.md)

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
api_instance = openshift.openshift.client.AuthorizationV1Api()

try: 
    api_response = api_instance.get_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthorizationV1Api->get_api_resources: %s\n" % e)
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

