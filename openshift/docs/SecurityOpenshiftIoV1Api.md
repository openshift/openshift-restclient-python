# openshift.client.SecurityOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_security_openshift_io_v1_namespaced_pod_security_policy_review**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_namespaced_pod_security_policy_review) | **POST** /apis/security.openshift.io/v1/namespaces/{namespace}/podsecuritypolicyreviews | 
[**create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review) | **POST** /apis/security.openshift.io/v1/namespaces/{namespace}/podsecuritypolicyselfsubjectreviews | 
[**create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review) | **POST** /apis/security.openshift.io/v1/namespaces/{namespace}/podsecuritypolicysubjectreviews | 
[**create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces) | **POST** /apis/security.openshift.io/v1/podsecuritypolicyreviews | 
[**create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces) | **POST** /apis/security.openshift.io/v1/podsecuritypolicyselfsubjectreviews | 
[**create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces**](SecurityOpenshiftIoV1Api.md#create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces) | **POST** /apis/security.openshift.io/v1/podsecuritypolicysubjectreviews | 
[**get_security_openshift_io_v1_api_resources**](SecurityOpenshiftIoV1Api.md#get_security_openshift_io_v1_api_resources) | **GET** /apis/security.openshift.io/v1/ | 


# **create_security_openshift_io_v1_namespaced_pod_security_policy_review**
> V1PodSecurityPolicyReview create_security_openshift_io_v1_namespaced_pod_security_policy_review(body, namespace, pretty=pretty)



create a PodSecurityPolicyReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicyReview() # V1PodSecurityPolicyReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_namespaced_pod_security_policy_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_namespaced_pod_security_policy_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicyReview**](V1PodSecurityPolicyReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicyReview**](V1PodSecurityPolicyReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review**
> V1PodSecurityPolicySelfSubjectReview create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review(body, namespace, pretty=pretty)



create a PodSecurityPolicySelfSubjectReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicySelfSubjectReview() # V1PodSecurityPolicySelfSubjectReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_namespaced_pod_security_policy_self_subject_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicySelfSubjectReview**](V1PodSecurityPolicySelfSubjectReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicySelfSubjectReview**](V1PodSecurityPolicySelfSubjectReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review**
> V1PodSecurityPolicySubjectReview create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review(body, namespace, pretty=pretty)



create a PodSecurityPolicySubjectReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicySubjectReview() # V1PodSecurityPolicySubjectReview | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_namespaced_pod_security_policy_subject_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicySubjectReview**](V1PodSecurityPolicySubjectReview.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicySubjectReview**](V1PodSecurityPolicySubjectReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces**
> V1PodSecurityPolicyReview create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces(body, pretty=pretty)



create a PodSecurityPolicyReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicyReview() # V1PodSecurityPolicyReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_pod_security_policy_review_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicyReview**](V1PodSecurityPolicyReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicyReview**](V1PodSecurityPolicyReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces**
> V1PodSecurityPolicySelfSubjectReview create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces(body, pretty=pretty)



create a PodSecurityPolicySelfSubjectReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicySelfSubjectReview() # V1PodSecurityPolicySelfSubjectReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_pod_security_policy_self_subject_review_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicySelfSubjectReview**](V1PodSecurityPolicySelfSubjectReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicySelfSubjectReview**](V1PodSecurityPolicySelfSubjectReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces**
> V1PodSecurityPolicySubjectReview create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces(body, pretty=pretty)



create a PodSecurityPolicySubjectReview

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()
body = openshift.client.V1PodSecurityPolicySubjectReview() # V1PodSecurityPolicySubjectReview | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->create_security_openshift_io_v1_pod_security_policy_subject_review_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PodSecurityPolicySubjectReview**](V1PodSecurityPolicySubjectReview.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1PodSecurityPolicySubjectReview**](V1PodSecurityPolicySubjectReview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_security_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.SecurityOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_security_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityOpenshiftIoV1Api->get_security_openshift_io_v1_api_resources: %s\n" % e)
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

