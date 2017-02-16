# V1BuildTriggerCause

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**generic_web_hook** | [**V1GenericWebHookCause**](V1GenericWebHookCause.md) | genericWebHook holds data about a builds generic webhook trigger. | [optional] 
**github_web_hook** | [**V1GitHubWebHookCause**](V1GitHubWebHookCause.md) | gitHubWebHook represents data for a GitHub webhook that fired a specific build. | [optional] 
**image_change_build** | [**V1ImageChangeCause**](V1ImageChangeCause.md) | imageChangeBuild stores information about an imagechange event that triggered a new build. | [optional] 
**message** | **str** | message is used to store a human readable message for why the build was triggered. E.g.: \&quot;Manually triggered by user\&quot;, \&quot;Configuration change\&quot;,etc. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


