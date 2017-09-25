# V1OAuthClient

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_max_age_seconds** | **int** | AccessTokenMaxAgeSeconds overrides the default access token max age for tokens granted to this openshift.openshift.client. 0 means no expiration. | [optional] 
**additional_secrets** | **list[str]** | AdditionalSecrets holds other secrets that may be used to identify the openshift.openshift.client.  This is useful for rotation and for service account token validation | [optional] 
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**grant_method** | **str** | GrantMethod determines how to handle grants for this openshift.openshift.client. If no method is provided, the cluster default grant handling method will be used. Valid grant handling methods are:  - auto:   always approves grant requests, useful for trusted openshift.openshift.clients  - prompt: prompts the end user for approval of grant requests, useful for third-party openshift.openshift.clients  - deny:   always denies grant requests, useful for black-listed openshift.openshift.clients | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.openshift.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**redirect_ur_is** | **list[str]** | RedirectURIs is the valid redirection URIs associated with a openshift.openshift.client | [optional] 
**respond_with_challenges** | **bool** | RespondWithChallenges indicates whether the openshift.openshift.client wants authentication needed responses made in the form of challenges instead of redirects | [optional] 
**scope_restrictions** | [**list[V1ScopeRestriction]**](V1ScopeRestriction.md) | ScopeRestrictions describes which scopes this openshift.openshift.client can request.  Each requested scope is checked against each restriction.  If any restriction matches, then the scope is allowed. If no restriction matches, then the scope is denied. | [optional] 
**secret** | **str** | Secret is the unique secret associated with a openshift.openshift.client | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


