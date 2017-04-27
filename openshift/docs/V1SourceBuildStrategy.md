# V1SourceBuildStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | env contains additional environment variables you want to pass into a builder container | [optional] 
**force_pull** | **bool** | forcePull describes if the builder should pull the images from registry prior to building. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled | 
**incremental** | **bool** | incremental flag forces the Source build to do incremental builds if true. | [optional] 
**pull_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries | [optional] 
**runtime_artifacts** | [**list[V1ImageSourcePath]**](V1ImageSourcePath.md) | runtimeArtifacts specifies a list of source/destination pairs that will be copied from the builder to the runtime image. sourcePath can be a file or directory. destinationDir must be a directory. destinationDir can also be empty or equal to \&quot;.\&quot;, in this case it just refers to the root of WORKDIR. This field and the feature it enables are in tech preview. | [optional] 
**runtime_image** | [**V1ObjectReference**](V1ObjectReference.md) | runtimeImage is an optional image that is used to run an application without unneeded dependencies installed. The building of the application is still done in the builder image but, post build, you can copy the needed artifacts in the runtime image for use. This field and the feature it enables are in tech preview. | [optional] 
**scripts** | **str** | scripts is the location of Source scripts | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


