# V1OAuthClient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_secrets** | **list[str]** | AdditionalSecrets holds other secrets that may be used to identify the openshift.client.  This is useful for rotation and for service account token validation | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**grant_method** | **str** | GrantMethod determines how to handle grants for this openshift.client. If no method is provided, the cluster default grant handling method will be used. Valid grant handling methods are:  - auto:   always approves grant requests, useful for trusted openshift.clients  - prompt: prompts the end user for approval of grant requests, useful for third-party openshift.clients  - deny:   always denies grant requests, useful for black-listed openshift.clients | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**redirect_ur_is** | **list[str]** | RedirectURIs is the valid redirection URIs associated with a openshift.client | [optional] 
**respond_with_challenges** | **bool** | RespondWithChallenges indicates whether the openshift.client wants authentication needed responses made in the form of challenges instead of redirects | [optional] 
**scope_restrictions** | [**list[V1ScopeRestriction]**](V1ScopeRestriction.md) | ScopeRestrictions describes which scopes this openshift.client can request.  Each requested scope is checked against each restriction.  If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied. | [optional] 
**secret** | **str** | Secret is the unique secret associated with a openshift.client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


