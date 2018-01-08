# V1TagReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Optional; if specified, annotations that are applied to images retrieved via ImageStreamTags. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | Optional; if specified, a reference to another image that this tag should point to. Valid values are ImageStreamTag, ImageStreamImage, and DockerImage. | [optional] 
**generation** | **int** | Generation is a counter that tracks mutations to the spec tag (user intent). When a tag reference is changed the generation is set to match the current stream generation (which is incremented every time spec is changed). Other processes in the system like the image importer observe that the generation of spec tag is newer than the generation recorded in the status and use that as a trigger to import the newest remote tag. To trigger a new import, openshift.clients may set this value to zero which will reset the generation to the latest stream generation. Legacy openshift.clients will send this value as nil which will be merged with the current tag generation. | [optional] 
**import_policy** | [**V1TagImportPolicy**](V1TagImportPolicy.md) | ImportPolicy is information that controls how images may be imported by the server. | [optional] 
**name** | **str** | Name of the tag | 
**reference** | **bool** | Reference states if the tag will be imported. Default value is false, which means the tag will be imported. | [optional] 
**reference_policy** | [**V1TagReferencePolicy**](V1TagReferencePolicy.md) | ReferencePolicy defines how other components should consume the image. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


