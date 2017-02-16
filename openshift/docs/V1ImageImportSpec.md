# V1ImageImportSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is the source of an image to import; only kind DockerImage is allowed | 
**import_policy** | [**V1TagImportPolicy**](V1TagImportPolicy.md) | ImportPolicy is the policy controlling how the image is imported | [optional] 
**include_manifest** | **bool** | IncludeManifest determines if the manifest for each image is returned in the response | [optional] 
**to** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | To is a tag in the current image stream to assign the imported image to, if name is not specified the default tag from from.name will be used | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


