# V1TLSConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_certificate** | **str** | caCertificate provides the cert authority certificate contents | [optional] 
**certificate** | **str** | certificate provides certificate contents | [optional] 
**destination_ca_certificate** | **str** | destinationCACertificate provides the contents of the ca certificate of the final destination.  When using reencrypt termination this file should be provided in order to have routers use it for health checks on the secure connection | [optional] 
**insecure_edge_termination_policy** | **str** | insecureEdgeTerminationPolicy indicates the desired behavior for insecure connections to a route. While each router may make its own decisions on which ports to expose, this is normally port 80.  * Allow - traffic is sent to the server on the insecure port (default) * Disable - no traffic is allowed on the insecure port. * Redirect - openshift.clients are redirected to the secure port. | [optional] 
**key** | **str** | key provides key file contents | [optional] 
**termination** | **str** | termination indicates termination type. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


