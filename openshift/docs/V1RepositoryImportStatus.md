# V1RepositoryImportStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_tags** | **list[str]** | AdditionalTags are tags that exist in the repository but were not imported because a maximum limit of automatic imports was applied. | [optional] 
**images** | [**list[V1ImageImportStatus]**](V1ImageImportStatus.md) | Images is a list of images successfully retrieved by the import of the repository. | [optional] 
**status** | [**UnversionedStatus**](UnversionedStatus.md) | Status reflects whether any failure occurred during import | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


