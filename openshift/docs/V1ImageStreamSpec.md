# V1ImageStreamSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_image_repository** | **str** | dockerImageRepository is optional, if specified this stream is backed by a Docker repository on this server Deprecated: This field is deprecated as of v3.7 and will be removed in a future release. Specify the source for the tags to be imported in each tag via the spec.tags.from reference instead. | [optional] 
**lookup_policy** | [**V1ImageLookupPolicy**](V1ImageLookupPolicy.md) | lookupPolicy controls how other resources reference images within this namespace. | [optional] 
**tags** | [**list[V1TagReference]**](V1TagReference.md) | tags map arbitrary string values to specific image locators | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


