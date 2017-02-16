# V1DeploymentConfigStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_replicas** | **int** | AvailableReplicas is the total number of available pods targeted by this deployment config. | 
**conditions** | [**list[V1DeploymentCondition]**](V1DeploymentCondition.md) | Conditions represents the latest available observations of a deployment config&#39;s current state. | [optional] 
**details** | [**V1DeploymentDetails**](V1DeploymentDetails.md) | Details are the reasons for the update to this deployment config. This could be based on a change made by the user or caused by an automatic trigger | [optional] 
**latest_version** | **int** | LatestVersion is used to determine whether the current deployment associated with a deployment config is out of sync. | 
**observed_generation** | **int** | ObservedGeneration is the most recent generation observed by the deployment config controller. | 
**ready_replicas** | **int** | Total number of ready pods targeted by this deployment. | [optional] 
**replicas** | **int** | Replicas is the total number of pods targeted by this deployment config. | 
**unavailable_replicas** | **int** | UnavailableReplicas is the total number of unavailable pods targeted by this deployment config. | 
**updated_replicas** | **int** | UpdatedReplicas is the total number of non-terminated pods targeted by this deployment config that have the desired template spec. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


