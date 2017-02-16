# V1RoleBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**group_names** | **list[str]** | GroupNames holds all the groups directly bound to the role. This field should only be specified when supporting legacy openshift.clients and servers. See Subjects for further details. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**role_ref** | [**V1ObjectReference**](V1ObjectReference.md) | RoleRef can only reference the current namespace and the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error. Since Policy is a singleton, this is sufficient knowledge to locate a role. | 
**subjects** | [**list[V1ObjectReference]**](V1ObjectReference.md) | Subjects hold object references to authorize with this rule. This field is ignored if UserNames or GroupNames are specified to support legacy openshift.clients and servers. Thus newer openshift.clients that do not need to support backwards compatibility should send only fully qualified Subjects and should omit the UserNames and GroupNames fields. Clients that need to support backwards compatibility can use this field to build the UserNames and GroupNames. | 
**user_names** | **list[str]** | UserNames holds all the usernames directly bound to the role. This field should only be specified when supporting legacy openshift.clients and servers. See Subjects for further details. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


