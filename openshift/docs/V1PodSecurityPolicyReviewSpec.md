# V1PodSecurityPolicyReviewSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_account_names** | **list[str]** | serviceAccountNames is an optional set of ServiceAccounts to run the check with. If serviceAccountNames is empty, the template.spec.serviceAccountName is used, unless it&#39;s empty, in which case \&quot;default\&quot; is used instead. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored. | [optional] 
**template** | [**V1PodTemplateSpec**](V1PodTemplateSpec.md) | template is the PodTemplateSpec to check. The template.spec.serviceAccountName field is used if serviceAccountNames is empty, unless the template.spec.serviceAccountName is empty, in which case \&quot;default\&quot; is used. If serviceAccountNames is specified, template.spec.serviceAccountName is ignored. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


