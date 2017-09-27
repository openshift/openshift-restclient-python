# V1RouteTargetReference

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The kind of target that the route is referring to. Currently, only &#39;Service&#39; is allowed | 
**name** | **str** | name of the service/target that is being referred to. e.g. name of the service | 
**weight** | **int** | weight as an integer between 0 and 256, default 1, that specifies the target&#39;s relative weight against other target reference objects. 0 suppresses requests to this backend. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


