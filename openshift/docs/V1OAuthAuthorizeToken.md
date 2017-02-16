# V1OAuthAuthorizeToken

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**openshift.client_name** | **str** | ClientName references the openshift.client that created this token. | [optional] 
**code_challenge** | **str** | CodeChallenge is the optional code_challenge associated with this authorization code, as described in rfc7636 | [optional] 
**code_challenge_method** | **str** | CodeChallengeMethod is the optional code_challenge_method associated with this authorization code, as described in rfc7636 | [optional] 
**expires_in** | **int** | ExpiresIn is the seconds from CreationTime before this token expires. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**redirect_uri** | **str** | RedirectURI is the redirection associated with the token. | [optional] 
**scopes** | **list[str]** | Scopes is an array of the requested scopes. | [optional] 
**state** | **str** | State data from request | [optional] 
**user_name** | **str** | UserName is the user name associated with this token | [optional] 
**user_uid** | **str** | UserUID is the unique UID associated with this token. UserUID and UserName must both match for this token to be valid. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


