# V1PodSecurityPolicySubjectReviewStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_by** | [**V1ObjectReference**](V1ObjectReference.md) | allowedBy is a reference to the rule that allows the PodTemplateSpec. A rule can be a SecurityContextConstraint or a PodSecurityPolicy A &#x60;nil&#x60;, indicates that it was denied. | [optional] 
**reason** | **str** | A machine-readable description of why this operation is in the \&quot;Failure\&quot; status. If this value is empty there is no information available. | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | template is the PodTemplateSpec after the defaulting is applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


