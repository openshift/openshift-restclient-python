# V1ImageStreamSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_image_repository** | **str** | dockerImageRepository is optional, if specified this stream is backed by a Docker repository on this server | [optional] 
**lookup_policy** | [**V1ImageLookupPolicy**](V1ImageLookupPolicy.md) | lookupPolicy controls how other resources reference images within this namespace. | [optional] 
**tags** | [**list[V1TagReference]**](V1TagReference.md) | tags map arbitrary string values to specific image locators | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


