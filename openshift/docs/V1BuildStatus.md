# V1BuildStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **bool** | cancelled describes if a cancel event was triggered for the build. | [optional] 
**completion_timestamp** | [**V1Time**](V1Time.md) | completionTimestamp is a timestamp representing the server time when this Build was finished, whether that build failed or succeeded.  It reflects the time at which the Pod running the Build terminated. It is represented in RFC3339 form and is in UTC. | [optional] 
**config** | [**V1ObjectReference**](V1ObjectReference.md) | config is an ObjectReference to the BuildConfig this Build is based on. | [optional] 
**duration** | **int** | duration contains time.Duration object describing build time. | [optional] 
**log_snippet** | **str** | logSnippet is the last few lines of the build log.  This value is only set for builds that failed. | [optional] 
**message** | **str** | message is a human-readable message indicating details about why the build has this status. | [optional] 
**output** | [**V1BuildStatusOutput**](V1BuildStatusOutput.md) | output describes the Docker image the build has produced. | [optional] 
**output_docker_image_reference** | **str** | outputDockerImageReference contains a reference to the Docker image that will be built by this build. Its value is computed from Build.Spec.Output.To, and should include the registry address, so that it can be used to push and pull the image. | [optional] 
**phase** | **str** | phase is the point in the build lifecycle. Possible values are \&quot;New\&quot;, \&quot;Pending\&quot;, \&quot;Running\&quot;, \&quot;Complete\&quot;, \&quot;Failed\&quot;, \&quot;Error\&quot;, and \&quot;Cancelled\&quot;. | 
**reason** | **str** | reason is a brief CamelCase string that describes any failure and is meant for machine parsing and tidy display in the CLI. | [optional] 
**stages** | [**list[V1StageInfo]**](V1StageInfo.md) | stages contains details about each stage that occurs during the build including start time, duration (in milliseconds), and the steps that occured within each stage. | [optional] 
**start_timestamp** | [**V1Time**](V1Time.md) | startTimestamp is a timestamp representing the server time when this Build started running in a Pod. It is represented in RFC3339 form and is in UTC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


