# V1ClusterResourceQuotaSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quota** | [**V1ResourceQuotaSpec**](V1ResourceQuotaSpec.md) | Quota defines the desired quota | 
**selector** | [**V1ClusterResourceQuotaSelector**](V1ClusterResourceQuotaSelector.md) | Selector is the selector used to match projects. It should only select active projects on the scale of dozens (though it can select many more less active projects).  These projects will contend on object creation through this resource. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


