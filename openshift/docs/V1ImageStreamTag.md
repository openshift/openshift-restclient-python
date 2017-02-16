# V1ImageStreamTag

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**conditions** | [**list[V1TagEventCondition]**](V1TagEventCondition.md) | Conditions is an array of conditions that apply to the image stream tag. | [optional] 
**generation** | **int** | Generation is the current generation of the tagged image - if tag is provided and this value is not equal to the tag generation, a user has requested an import that has not completed, or Conditions will be filled out indicating any error. | 
**image** | [**V1Image**](V1Image.md) | Image associated with the ImageStream and tag. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**tag** | [**V1TagReference**](V1TagReference.md) | Tag is the spec tag associated with this image stream tag, and it may be null if only pushes have occurred to this image stream. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


