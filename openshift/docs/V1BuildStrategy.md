# V1BuildStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_strategy** | [**V1CustomBuildStrategy**](V1CustomBuildStrategy.md) | customStrategy holds the parameters to the Custom build strategy | [optional] 
**docker_strategy** | [**V1DockerBuildStrategy**](V1DockerBuildStrategy.md) | dockerStrategy holds the parameters to the Docker build strategy. | [optional] 
**jenkins_pipeline_strategy** | [**V1JenkinsPipelineBuildStrategy**](V1JenkinsPipelineBuildStrategy.md) | JenkinsPipelineStrategy holds the parameters to the Jenkins Pipeline build strategy. This strategy is in tech preview. | [optional] 
**source_strategy** | [**V1SourceBuildStrategy**](V1SourceBuildStrategy.md) | sourceStrategy holds the parameters to the Source build strategy. | [optional] 
**type** | **str** | type is the kind of build strategy. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


