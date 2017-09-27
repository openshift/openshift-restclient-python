# V1ImageStreamStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docker_image_repository** | **str** | DockerImageRepository represents the effective location this stream may be accessed at. May be empty until the server determines where the repository is located | 
**public_docker_image_repository** | **str** | PublicDockerImageRepository represents the public location from where the image can be pulled outside the cluster. This field may be empty if the administrator has not exposed the integrated registry externally. | [optional] 
**tags** | [**list[V1NamedTagEventList]**](V1NamedTagEventList.md) | Tags are a historical record of images associated with each tag. The first entry in the TagEvent array is the currently tagged image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


