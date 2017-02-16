# V1ImageSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | from is a reference to an ImageStreamTag, ImageStreamImage, or DockerImage to copy source from. | 
**paths** | [**list[V1ImageSourcePath]**](V1ImageSourcePath.md) | paths is a list of source and destination paths to copy from the image. | 
**pull_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | pullSecret is a reference to a secret to be used to pull the image from a registry If the image is pulled from the OpenShift registry, this field does not need to be set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


