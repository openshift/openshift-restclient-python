# V1TagReferencePolicy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type determines how the image pull spec should be transformed when the image stream tag is used in deployment config triggers or new builds. The default value is &#x60;Source&#x60;, indicating the original location of the image should be used (if imported). The user may also specify &#x60;Local&#x60;, indicating that the pull spec should point to the integrated Docker registry and leverage the registry&#39;s ability to proxy the pull to an upstream registry. &#x60;Local&#x60; allows the credentials used to pull this image to be managed from the image stream&#39;s namespace, so others on the platform can access a remote image but have no access to the remote secret. It also allows the image layers to be mirrored into the local registry which the images can still be pulled even if the upstream registry is unavailable. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


