# V1ImageStreamImportSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**images** | [**list[V1ImageImportSpec]**](V1ImageImportSpec.md) | Images are a list of individual images to import. | [optional] 
**_import** | **bool** | Import indicates whether to perform an import - if so, the specified tags are set on the spec and status of the image stream defined by the type meta. | 
**repository** | [**V1RepositoryImportSpec**](V1RepositoryImportSpec.md) | Repository is an optional import of an entire Docker image repository. A maximum limit on the number of tags imported this way is imposed by the server. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


