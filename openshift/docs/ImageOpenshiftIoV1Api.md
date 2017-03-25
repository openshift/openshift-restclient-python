# openshift.client.ImageOpenshiftIoV1Api

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image) | **POST** /apis/image.openshift.io/v1/images | 
[**create_image_openshift_io_v1_image_signature**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image_signature) | **POST** /apis/image.openshift.io/v1/imagesignatures | 
[**create_image_openshift_io_v1_image_stream_for_all_namespaces**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image_stream_for_all_namespaces) | **POST** /apis/image.openshift.io/v1/imagestreams | 
[**create_image_openshift_io_v1_image_stream_import_for_all_namespaces**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image_stream_import_for_all_namespaces) | **POST** /apis/image.openshift.io/v1/imagestreamimports | 
[**create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces) | **POST** /apis/image.openshift.io/v1/imagestreammappings | 
[**create_image_openshift_io_v1_image_stream_tag_for_all_namespaces**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_image_stream_tag_for_all_namespaces) | **POST** /apis/image.openshift.io/v1/imagestreamtags | 
[**create_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_namespaced_image_stream) | **POST** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams | 
[**create_image_openshift_io_v1_namespaced_image_stream_import**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_namespaced_image_stream_import) | **POST** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamimports | 
[**create_image_openshift_io_v1_namespaced_image_stream_mapping**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_namespaced_image_stream_mapping) | **POST** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreammappings | 
[**create_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#create_image_openshift_io_v1_namespaced_image_stream_tag) | **POST** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags | 
[**delete_image_openshift_io_v1_collection_image**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_collection_image) | **DELETE** /apis/image.openshift.io/v1/images | 
[**delete_image_openshift_io_v1_collection_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_collection_namespaced_image_stream) | **DELETE** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams | 
[**delete_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_image) | **DELETE** /apis/image.openshift.io/v1/images/{name} | 
[**delete_image_openshift_io_v1_image_signature**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_image_signature) | **DELETE** /apis/image.openshift.io/v1/imagesignatures/{name} | 
[**delete_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_namespaced_image_stream) | **DELETE** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name} | 
[**delete_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#delete_image_openshift_io_v1_namespaced_image_stream_tag) | **DELETE** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name} | 
[**get_image_openshift_io_v1_api_resources**](ImageOpenshiftIoV1Api.md#get_image_openshift_io_v1_api_resources) | **GET** /apis/image.openshift.io/v1/ | 
[**list_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#list_image_openshift_io_v1_image) | **GET** /apis/image.openshift.io/v1/images | 
[**list_image_openshift_io_v1_image_stream_for_all_namespaces**](ImageOpenshiftIoV1Api.md#list_image_openshift_io_v1_image_stream_for_all_namespaces) | **GET** /apis/image.openshift.io/v1/imagestreams | 
[**list_image_openshift_io_v1_image_stream_tag_for_all_namespaces**](ImageOpenshiftIoV1Api.md#list_image_openshift_io_v1_image_stream_tag_for_all_namespaces) | **GET** /apis/image.openshift.io/v1/imagestreamtags | 
[**list_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#list_image_openshift_io_v1_namespaced_image_stream) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams | 
[**list_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#list_image_openshift_io_v1_namespaced_image_stream_tag) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags | 
[**patch_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#patch_image_openshift_io_v1_image) | **PATCH** /apis/image.openshift.io/v1/images/{name} | 
[**patch_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#patch_image_openshift_io_v1_namespaced_image_stream) | **PATCH** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name} | 
[**patch_image_openshift_io_v1_namespaced_image_stream_status**](ImageOpenshiftIoV1Api.md#patch_image_openshift_io_v1_namespaced_image_stream_status) | **PATCH** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/status | 
[**patch_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#patch_image_openshift_io_v1_namespaced_image_stream_tag) | **PATCH** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name} | 
[**read_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_image) | **GET** /apis/image.openshift.io/v1/images/{name} | 
[**read_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_namespaced_image_stream) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name} | 
[**read_image_openshift_io_v1_namespaced_image_stream_image**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_namespaced_image_stream_image) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamimages/{name} | 
[**read_image_openshift_io_v1_namespaced_image_stream_status**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_namespaced_image_stream_status) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/status | 
[**read_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_namespaced_image_stream_tag) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name} | 
[**read_image_openshift_io_v1_namespaced_secret_list_secrets**](ImageOpenshiftIoV1Api.md#read_image_openshift_io_v1_namespaced_secret_list_secrets) | **GET** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/secrets | 
[**replace_image_openshift_io_v1_image**](ImageOpenshiftIoV1Api.md#replace_image_openshift_io_v1_image) | **PUT** /apis/image.openshift.io/v1/images/{name} | 
[**replace_image_openshift_io_v1_namespaced_image_stream**](ImageOpenshiftIoV1Api.md#replace_image_openshift_io_v1_namespaced_image_stream) | **PUT** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name} | 
[**replace_image_openshift_io_v1_namespaced_image_stream_status**](ImageOpenshiftIoV1Api.md#replace_image_openshift_io_v1_namespaced_image_stream_status) | **PUT** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreams/{name}/status | 
[**replace_image_openshift_io_v1_namespaced_image_stream_tag**](ImageOpenshiftIoV1Api.md#replace_image_openshift_io_v1_namespaced_image_stream_tag) | **PUT** /apis/image.openshift.io/v1/namespaces/{namespace}/imagestreamtags/{name} | 


# **create_image_openshift_io_v1_image**
> V1Image create_image_openshift_io_v1_image(body, pretty=pretty)



create an Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1Image() # V1Image | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1Image**](V1Image.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_image_signature**
> V1ImageSignature create_image_openshift_io_v1_image_signature(body, pretty=pretty)



create an ImageSignature

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageSignature() # V1ImageSignature | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image_signature(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageSignature**](V1ImageSignature.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageSignature**](V1ImageSignature.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_image_stream_for_all_namespaces**
> V1ImageStream create_image_openshift_io_v1_image_stream_for_all_namespaces(body, pretty=pretty)



create an ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image_stream_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image_stream_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_image_stream_import_for_all_namespaces**
> V1ImageStreamImport create_image_openshift_io_v1_image_stream_import_for_all_namespaces(body, pretty=pretty)



create an ImageStreamImport

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStreamImport() # V1ImageStreamImport | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image_stream_import_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image_stream_import_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamImport**](V1ImageStreamImport.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImport**](V1ImageStreamImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces**
> V1ImageStreamMapping create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces(body, pretty=pretty)



create an ImageStreamMapping

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStreamMapping() # V1ImageStreamMapping | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image_stream_mapping_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamMapping**](V1ImageStreamMapping.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamMapping**](V1ImageStreamMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_image_stream_tag_for_all_namespaces**
> V1ImageStreamTag create_image_openshift_io_v1_image_stream_tag_for_all_namespaces(body, pretty=pretty)



create an ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStreamTag() # V1ImageStreamTag | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_image_stream_tag_for_all_namespaces(body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_image_stream_tag_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamTag**](V1ImageStreamTag.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_namespaced_image_stream**
> V1ImageStream create_image_openshift_io_v1_namespaced_image_stream(namespace, body, pretty=pretty)



create an ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_namespaced_image_stream(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_namespaced_image_stream_import**
> V1ImageStreamImport create_image_openshift_io_v1_namespaced_image_stream_import(body, namespace, pretty=pretty)



create an ImageStreamImport

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStreamImport() # V1ImageStreamImport | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_namespaced_image_stream_import(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_namespaced_image_stream_import: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamImport**](V1ImageStreamImport.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImport**](V1ImageStreamImport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_namespaced_image_stream_mapping**
> V1ImageStreamMapping create_image_openshift_io_v1_namespaced_image_stream_mapping(body, namespace, pretty=pretty)



create an ImageStreamMapping

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
body = openshift.client.V1ImageStreamMapping() # V1ImageStreamMapping | 
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_namespaced_image_stream_mapping(body, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_namespaced_image_stream_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ImageStreamMapping**](V1ImageStreamMapping.md)|  | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamMapping**](V1ImageStreamMapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_image_openshift_io_v1_namespaced_image_stream_tag**
> V1ImageStreamTag create_image_openshift_io_v1_namespaced_image_stream_tag(namespace, body, pretty=pretty)



create an ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1ImageStreamTag() # V1ImageStreamTag | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.create_image_openshift_io_v1_namespaced_image_stream_tag(namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->create_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1ImageStreamTag**](V1ImageStreamTag.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_collection_image**
> UnversionedStatus delete_image_openshift_io_v1_collection_image(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_collection_image(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_collection_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_collection_namespaced_image_stream**
> UnversionedStatus delete_image_openshift_io_v1_collection_namespaced_image_stream(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



delete collection of ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_collection_namespaced_image_stream(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_collection_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_image**
> UnversionedStatus delete_image_openshift_io_v1_image(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete an Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the Image
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_image(name, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_image_signature**
> UnversionedStatus delete_image_openshift_io_v1_image_signature(name, pretty=pretty)



delete an ImageSignature

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageSignature
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_image_signature(name, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_image_signature: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageSignature | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_namespaced_image_stream**
> UnversionedStatus delete_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)



delete an ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1DeleteOptions() # V1DeleteOptions | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
grace_period_seconds = 56 # int | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. (optional)
orphan_dependents = true # bool | Should the dependent objects be orphaned. If true/false, the \"orphan\" finalizer will be added to/removed from the object's finalizers list. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty, grace_period_seconds=grace_period_seconds, orphan_dependents=orphan_dependents)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1DeleteOptions**](V1DeleteOptions.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **grace_period_seconds** | **int**| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. | [optional] 
 **orphan_dependents** | **bool**| Should the dependent objects be orphaned. If true/false, the \&quot;orphan\&quot; finalizer will be added to/removed from the object&#39;s finalizers list. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_image_openshift_io_v1_namespaced_image_stream_tag**
> UnversionedStatus delete_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, pretty=pretty)



delete an ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStreamTag
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.delete_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->delete_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStreamTag | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**UnversionedStatus**](UnversionedStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_openshift_io_v1_api_resources**
> UnversionedAPIResourceList get_image_openshift_io_v1_api_resources()



get available resources

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()

try: 
    api_response = api_instance.get_image_openshift_io_v1_api_resources()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->get_image_openshift_io_v1_api_resources: %s\n" % e)
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

# **list_image_openshift_io_v1_image**
> V1ImageList list_image_openshift_io_v1_image(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_image_openshift_io_v1_image(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->list_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ImageList**](V1ImageList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_openshift_io_v1_image_stream_for_all_namespaces**
> V1ImageStreamList list_image_openshift_io_v1_image_stream_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_image_openshift_io_v1_image_stream_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->list_image_openshift_io_v1_image_stream_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ImageStreamList**](V1ImageStreamList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_openshift_io_v1_image_stream_tag_for_all_namespaces**
> V1ImageStreamTagList list_image_openshift_io_v1_image_stream_tag_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list objects of kind ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_image_openshift_io_v1_image_stream_tag_for_all_namespaces(pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->list_image_openshift_io_v1_image_stream_tag_for_all_namespaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ImageStreamTagList**](V1ImageStreamTagList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_openshift_io_v1_namespaced_image_stream**
> V1ImageStreamList list_image_openshift_io_v1_namespaced_image_stream(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list or watch objects of kind ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_image_openshift_io_v1_namespaced_image_stream(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->list_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ImageStreamList**](V1ImageStreamList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_image_openshift_io_v1_namespaced_image_stream_tag**
> V1ImageStreamTagList list_image_openshift_io_v1_namespaced_image_stream_tag(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



list objects of kind ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.list_image_openshift_io_v1_namespaced_image_stream_tag(namespace, pretty=pretty, field_selector=field_selector, label_selector=label_selector, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->list_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1ImageStreamTagList**](V1ImageStreamTagList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf, application/json;stream=watch, application/vnd.kubernetes.protobuf;stream=watch

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_image_openshift_io_v1_image**
> V1Image patch_image_openshift_io_v1_image(name, body, pretty=pretty)



partially update the specified Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the Image
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_image_openshift_io_v1_image(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->patch_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_image_openshift_io_v1_namespaced_image_stream**
> V1ImageStream patch_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty)



partially update the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->patch_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_image_openshift_io_v1_namespaced_image_stream_status**
> V1ImageStream patch_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, body, pretty=pretty)



partially update status of the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->patch_image_openshift_io_v1_namespaced_image_stream_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_image_openshift_io_v1_namespaced_image_stream_tag**
> V1ImageStreamTag patch_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, body, pretty=pretty)



partially update the specified ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStreamTag
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.UnversionedPatch() # UnversionedPatch | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.patch_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->patch_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStreamTag | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**UnversionedPatch**](UnversionedPatch.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/merge-patch+json, application/strategic-merge-patch+json
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_image**
> V1Image read_image_openshift_io_v1_image(name, pretty=pretty, exact=exact, export=export)



read the specified Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the Image
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_image(name, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_namespaced_image_stream**
> V1ImageStream read_image_openshift_io_v1_namespaced_image_stream(name, namespace, pretty=pretty, exact=exact, export=export)



read the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
exact = true # bool | Should the export be exact.  Exact export maintains cluster-specific fields like 'Namespace' (optional)
export = true # bool | Should this value be exported.  Export strips fields that a user can not specify. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_namespaced_image_stream(name, namespace, pretty=pretty, exact=exact, export=export)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **exact** | **bool**| Should the export be exact.  Exact export maintains cluster-specific fields like &#39;Namespace&#39; | [optional] 
 **export** | **bool**| Should this value be exported.  Export strips fields that a user can not specify. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_namespaced_image_stream_image**
> V1ImageStreamImage read_image_openshift_io_v1_namespaced_image_stream_image(name, namespace, pretty=pretty)



read the specified ImageStreamImage

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStreamImage
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_namespaced_image_stream_image(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_namespaced_image_stream_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStreamImage | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamImage**](V1ImageStreamImage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_namespaced_image_stream_status**
> V1ImageStream read_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, pretty=pretty)



read status of the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_namespaced_image_stream_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_namespaced_image_stream_tag**
> V1ImageStreamTag read_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, pretty=pretty)



read the specified ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStreamTag
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStreamTag | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_image_openshift_io_v1_namespaced_secret_list_secrets**
> V1SecretList read_image_openshift_io_v1_namespaced_secret_list_secrets(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)



read secrets of the specified SecretList

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the SecretList
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
field_selector = 'field_selector_example' # str | A selector to restrict the list of returned objects by their fields. Defaults to everything. (optional)
label_selector = 'label_selector_example' # str | A selector to restrict the list of returned objects by their labels. Defaults to everything. (optional)
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)
resource_version = 'resource_version_example' # str | When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. (optional)
timeout_seconds = 56 # int | Timeout for the list/watch call. (optional)
watch = true # bool | Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. (optional)

try: 
    api_response = api_instance.read_image_openshift_io_v1_namespaced_secret_list_secrets(name, namespace, field_selector=field_selector, label_selector=label_selector, pretty=pretty, resource_version=resource_version, timeout_seconds=timeout_seconds, watch=watch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->read_image_openshift_io_v1_namespaced_secret_list_secrets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the SecretList | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **field_selector** | **str**| A selector to restrict the list of returned objects by their fields. Defaults to everything. | [optional] 
 **label_selector** | **str**| A selector to restrict the list of returned objects by their labels. Defaults to everything. | [optional] 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 
 **resource_version** | **str**| When specified with a watch call, shows changes that occur after that particular version of a resource. Defaults to changes from the beginning of history. | [optional] 
 **timeout_seconds** | **int**| Timeout for the list/watch call. | [optional] 
 **watch** | **bool**| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion. | [optional] 

### Return type

[**V1SecretList**](V1SecretList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_image_openshift_io_v1_image**
> V1Image replace_image_openshift_io_v1_image(name, body, pretty=pretty)



replace the specified Image

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the Image
body = openshift.client.V1Image() # V1Image | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_image_openshift_io_v1_image(name, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->replace_image_openshift_io_v1_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the Image | 
 **body** | [**V1Image**](V1Image.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1Image**](V1Image.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_image_openshift_io_v1_namespaced_image_stream**
> V1ImageStream replace_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty)



replace the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_image_openshift_io_v1_namespaced_image_stream(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->replace_image_openshift_io_v1_namespaced_image_stream: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_image_openshift_io_v1_namespaced_image_stream_status**
> V1ImageStream replace_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, body, pretty=pretty)



replace status of the specified ImageStream

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStream
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1ImageStream() # V1ImageStream | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_image_openshift_io_v1_namespaced_image_stream_status(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->replace_image_openshift_io_v1_namespaced_image_stream_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStream | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1ImageStream**](V1ImageStream.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStream**](V1ImageStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_image_openshift_io_v1_namespaced_image_stream_tag**
> V1ImageStreamTag replace_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, body, pretty=pretty)



replace the specified ImageStreamTag

### Example 
```python
from __future__ import print_statement
import time
import openshift.client
from kubernetes.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openshift.client.ImageOpenshiftIoV1Api()
name = 'name_example' # str | name of the ImageStreamTag
namespace = 'namespace_example' # str | object name and auth scope, such as for teams and projects
body = openshift.client.V1ImageStreamTag() # V1ImageStreamTag | 
pretty = 'pretty_example' # str | If 'true', then the output is pretty printed. (optional)

try: 
    api_response = api_instance.replace_image_openshift_io_v1_namespaced_image_stream_tag(name, namespace, body, pretty=pretty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImageOpenshiftIoV1Api->replace_image_openshift_io_v1_namespaced_image_stream_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the ImageStreamTag | 
 **namespace** | **str**| object name and auth scope, such as for teams and projects | 
 **body** | [**V1ImageStreamTag**](V1ImageStreamTag.md)|  | 
 **pretty** | **str**| If &#39;true&#39;, then the output is pretty printed. | [optional] 

### Return type

[**V1ImageStreamTag**](V1ImageStreamTag.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json, application/yaml, application/vnd.kubernetes.protobuf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

