# V1RecreateDeploymentStrategyParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mid** | [**V1LifecycleHook**](V1LifecycleHook.md) | Mid is a lifecycle hook which is executed while the deployment is scaled down to zero before the first new pod is created. All LifecycleHookFailurePolicy values are supported. | [optional] 
**post** | [**V1LifecycleHook**](V1LifecycleHook.md) | Post is a lifecycle hook which is executed after the strategy has finished all deployment logic. All LifecycleHookFailurePolicy values are supported. | [optional] 
**pre** | [**V1LifecycleHook**](V1LifecycleHook.md) | Pre is a lifecycle hook which is executed before the strategy manipulates the deployment. All LifecycleHookFailurePolicy values are supported. | [optional] 
**timeout_seconds** | **int** | TimeoutSeconds is the time to wait for updates before giving up. If the value is nil, a default will be used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


