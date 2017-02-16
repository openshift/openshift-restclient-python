# V1PolicyBinding

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**last_modified** | [**UnversionedTime**](UnversionedTime.md) | LastModified is the last time that any part of the PolicyBinding was created, updated, or deleted | 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**policy_ref** | [**V1ObjectReference**](V1ObjectReference.md) | PolicyRef is a reference to the Policy that contains all the Roles that this PolicyBinding&#39;s RoleBindings may reference | 
**role_bindings** | [**list[V1NamedRoleBinding]**](V1NamedRoleBinding.md) | RoleBindings holds all the RoleBindings held by this PolicyBinding, mapped by RoleBinding.Name | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


