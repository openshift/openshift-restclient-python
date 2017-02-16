# V1DeploymentTriggerImageChangeParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | **bool** | Automatic means that the detection of a new tag value should result in an image update inside the pod template. | [optional] 
**container_names** | **list[str]** | ContainerNames is used to restrict tag updates to the specified set of container names in a pod. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | From is a reference to an image stream tag to watch for changes. From.Name is the only required subfield - if From.Namespace is blank, the namespace of the current deployment trigger will be used. | 
**last_triggered_image** | **str** | LastTriggeredImage is the last image to be triggered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


