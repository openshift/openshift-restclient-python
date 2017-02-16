# V1PodSecurityPolicySubjectReviewSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **list[str]** | groups is the groups you&#39;re testing for. | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | template is the PodTemplateSpec to check. If template.spec.serviceAccountName is empty it will not be defaulted. If its non-empty, it will be checked. | 
**user** | **str** | user is the user you&#39;re testing for. If you specify \&quot;user\&quot; but not \&quot;group\&quot;, then is it interpreted as \&quot;What if user were not a member of any groups. If user and groups are empty, then the check is performed using *only* the serviceAccountName in the template. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


