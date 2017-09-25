# V1BuildRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#resources | [optional] 
**binary** | [**V1BinaryBuildSource**](V1BinaryBuildSource.md) | binary indicates a request to build from a binary provided to the builder | [optional] 
**docker_strategy_options** | [**V1DockerStrategyOptions**](V1DockerStrategyOptions.md) | DockerStrategyOptions contains additional docker-strategy specific options for the build | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | env contains additional environment variables you want to pass into a builder container. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | from is the reference to the ImageStreamTag that triggered the build. | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.openshift.client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/api-conventions.md#types-kinds | [optional] 
**last_version** | **int** | lastVersion (optional) is the LastVersion of the BuildConfig that was used to generate the build. If the BuildConfig in the generator doesn&#39;t match, a build will not be generated. | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | metadata for BuildRequest. | [optional] 
**revision** | [**V1SourceRevision**](V1SourceRevision.md) | revision is the information from the source for a specific repo snapshot. | [optional] 
**source_strategy_options** | [**V1SourceStrategyOptions**](V1SourceStrategyOptions.md) | SourceStrategyOptions contains additional source-strategy specific options for the build | [optional] 
**triggered_by** | [**list[V1BuildTriggerCause]**](V1BuildTriggerCause.md) | triggeredBy describes which triggers started the most recent update to the build configuration and contains information about those triggers. | 
**triggered_by_image** | [**V1ObjectReference**](V1ObjectReference.md) | triggeredByImage is the Image that triggered this build. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


