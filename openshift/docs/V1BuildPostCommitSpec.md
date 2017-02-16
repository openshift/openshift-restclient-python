# V1BuildPostCommitSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | args is a list of arguments that are provided to either Command, Script or the Docker image&#39;s default entrypoint. The arguments are placed immediately after the command to be run. | [optional] 
**command** | **list[str]** | command is the command to run. It may not be specified with Script. This might be needed if the image doesn&#39;t have &#x60;/bin/sh&#x60;, or if you do not want to use a shell. In all other cases, using Script might be more convenient. | [optional] 
**script** | **str** | script is a shell script to be run with &#x60;/bin/sh -ic&#x60;. It may not be specified with Command. Use Script when a shell script is appropriate to execute the post build hook, for example for running unit tests with &#x60;rake test&#x60;. If you need control over the image entrypoint, or if the image does not have &#x60;/bin/sh&#x60;, use Command and/or Args. The &#x60;-i&#x60; flag is needed to support CentOS and RHEL images that use Software Collections (SCL), in order to have the appropriate collections enabled in the shell. E.g., in the Ruby image, this is necessary to make &#x60;ruby&#x60;, &#x60;bundle&#x60; and other binaries available in the PATH. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


