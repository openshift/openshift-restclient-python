# V1PodSecurityPolicySelfSubjectReview

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**spec** | [**V1PodSecurityPolicySelfSubjectReviewSpec**](V1PodSecurityPolicySelfSubjectReviewSpec.md) | spec defines specification the PodSecurityPolicySelfSubjectReview. | 
**status** | [**V1PodSecurityPolicySubjectReviewStatus**](V1PodSecurityPolicySubjectReviewStatus.md) | status represents the current information/status for the PodSecurityPolicySelfSubjectReview. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


