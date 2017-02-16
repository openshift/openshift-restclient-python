# V1RepositoryImportSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is the source for the image repository to import; only kind DockerImage and a name of a Docker image repository is allowed | 
**import_policy** | [**V1TagImportPolicy**](V1TagImportPolicy.md) | ImportPolicy is the policy controlling how the image is imported | [optional] 
**include_manifest** | **bool** | IncludeManifest determines if the manifest for each image is returned in the response | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


