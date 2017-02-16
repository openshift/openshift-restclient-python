# V1ClusterResourceQuotaStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespaces** | [**list[V1ResourceQuotaStatusByNamespace]**](V1ResourceQuotaStatusByNamespace.md) | Namespaces slices the usage by project.  This division allows for quick resolution of deletion reconciliation inside of a single project without requiring a recalculation across all projects.  This can be used to pull the deltas for a given project. | 
**total** | [**V1ResourceQuotaStatus**](V1ResourceQuotaStatus.md) | Total defines the actual enforced quota and its current usage across all projects | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


