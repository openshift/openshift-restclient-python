# V1RunAsUserStrategyOptions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type is the strategy that will dictate what RunAsUser is used in the SecurityContext. | [optional] 
**uid** | **int** | UID is the user id that containers must run as.  Required for the MustRunAs strategy if not using namespace/service account allocated uids. | [optional] 
**uid_range_max** | **int** | UIDRangeMax defines the max value for a strategy that allocates by range. | [optional] 
**uid_range_min** | **int** | UIDRangeMin defines the min value for a strategy that allocates by range. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


