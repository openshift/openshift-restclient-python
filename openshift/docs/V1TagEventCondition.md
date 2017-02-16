# V1TagEventCondition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generation** | **int** | Generation is the spec tag generation that this status corresponds to | 
**last_transition_time** | [**UnversionedTime**](UnversionedTime.md) | LastTransitionTIme is the time the condition transitioned from one status to another. | [optional] 
**message** | **str** | Message is a human readable description of the details about last transition, complementing reason. | [optional] 
**reason** | **str** | Reason is a brief machine readable explanation for the condition&#39;s last transition. | [optional] 
**status** | **str** | Status of the condition, one of True, False, Unknown. | 
**type** | **str** | Type of tag event condition, currently only ImportSuccess | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


