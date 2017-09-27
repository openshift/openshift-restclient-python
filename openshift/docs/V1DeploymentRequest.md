# V1DeploymentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**exclude_triggers** | **list[str]** | ExcludeTriggers instructs the instantiator to avoid processing the specified triggers. This field overrides the triggers from latest and allows openshift.clients to control specific logic. This field is ignored if not specified. | [optional] 
**force** | **bool** | Force will try to force a new deployment to run. If the deployment config is paused, then setting this to true will return an Invalid error. | 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**latest** | **bool** | Latest will update the deployment config with the latest state from all triggers. | 
**name** | **str** | Name of the deployment config for requesting a new deployment. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


