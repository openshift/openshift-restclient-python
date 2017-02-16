# V1DeploymentStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_deadline_seconds** | **int** | ActiveDeadlineSeconds is the duration in seconds that the deployer pods for this deployment config may be active on a node before the system actively tries to terminate them. | [optional] 
**annotations** | **dict(str, str)** | Annotations is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods. | [optional] 
**custom_params** | [**V1CustomDeploymentStrategyParams**](V1CustomDeploymentStrategyParams.md) | CustomParams are the input to the Custom deployment strategy, and may also be specified for the Recreate and Rolling strategies to customize the execution process that runs the deployment. | [optional] 
**labels** | **dict(str, str)** | Labels is a set of key, value pairs added to custom deployer and lifecycle pre/post hook pods. | [optional] 
**recreate_params** | [**V1RecreateDeploymentStrategyParams**](V1RecreateDeploymentStrategyParams.md) | RecreateParams are the input to the Recreate deployment strategy. | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | Resources contains resource requirements to execute the deployment and any hooks. | [optional] 
**rolling_params** | [**V1RollingDeploymentStrategyParams**](V1RollingDeploymentStrategyParams.md) | RollingParams are the input to the Rolling deployment strategy. | [optional] 
**type** | **str** | Type is the name of a deployment strategy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


