# V1HostSubnet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**egress_i_ps** | **list[str]** | EgressIPs is the list of automatic egress IP addresses currently hosted by this node | [optional] 
**host** | **str** | Host is the name of the node. (This is the same as the object&#39;s name, but both fields must be set.) | 
**host_ip** | **str** | HostIP is the IP address to be used as a VTEP by other nodes in the overlay network | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**subnet** | **str** | Subnet is the CIDR range of the overlay network assigned to the node for its pods | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


