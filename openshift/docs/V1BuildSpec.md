# V1BuildSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_deadline_seconds** | **int** | completionDeadlineSeconds is an optional duration in seconds, counted from the time when a build pod gets scheduled in the system, that the build may be active on a node before the system actively tries to terminate the build; value must be positive integer | [optional] 
**node_selector** | **dict(str, str)** | nodeSelector is a selector which must be true for the build pod to fit on a node If nil, it can be overridden by default build nodeselector values for the cluster. If set to an empty map or a map with any values, default build nodeselector values are ignored. | 
**output** | [**V1BuildOutput**](V1BuildOutput.md) | output describes the Docker image the Strategy should produce. | [optional] 
**post_commit** | [**V1BuildPostCommitSpec**](V1BuildPostCommitSpec.md) | postCommit is a build hook executed after the build output image is committed, before it is pushed to a registry. | [optional] 
**resources** | [**V1ResourceRequirements**](V1ResourceRequirements.md) | resources computes resource requirements to execute the build. | [optional] 
**revision** | [**V1SourceRevision**](V1SourceRevision.md) | revision is the information from the source for a specific repo snapshot. This is optional. | [optional] 
**service_account** | **str** | serviceAccount is the name of the ServiceAccount to use to run the pod created by this build. The pod will be allowed to use secrets referenced by the ServiceAccount | [optional] 
**source** | [**V1BuildSource**](V1BuildSource.md) | source describes the SCM in use. | [optional] 
**strategy** | [**V1BuildStrategy**](V1BuildStrategy.md) | strategy defines how to perform a build. | 
**triggered_by** | [**list[V1BuildTriggerCause]**](V1BuildTriggerCause.md) | triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


