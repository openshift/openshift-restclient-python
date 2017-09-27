# V1DockerBuildStrategy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_args** | [**list[V1EnvVar]**](V1EnvVar.md) | buildArgs contains build arguments that will be resolved in the Dockerfile.  See https://docs.docker.com/engine/reference/builder/#/arg for more details. | [optional] 
**dockerfile_path** | **str** | dockerfilePath is the path of the Dockerfile that will be used to build the Docker image, relative to the root of the context (contextDir). | [optional] 
**env** | [**list[V1EnvVar]**](V1EnvVar.md) | env contains additional environment variables you want to pass into a builder container. | [optional] 
**force_pull** | **bool** | forcePull describes if the builder should pull the images from registry prior to building. | [optional] 
**_from** | [**V1ObjectReference**](V1ObjectReference.md) | from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled the resulting image will be used in the FROM line of the Dockerfile for this build. | [optional] 
**image_optimization_policy** | **str** | imageOptimizationPolicy describes what optimizations the system can use when building images to reduce the final size or time spent building the image. The default policy is &#39;None&#39; which means the final build image will be equivalent to an image created by the Docker build API. The experimental policy &#39;SkipLayers&#39; will avoid commiting new layers in between each image step, and will fail if the Dockerfile cannot provide compatibility with the &#39;None&#39; policy. An additional experimental policy &#39;SkipLayersAndWarn&#39; is the same as &#39;SkipLayers&#39; but simply warns if compatibility cannot be preserved. | [optional] 
**no_cache** | **bool** | noCache if set to true indicates that the docker build must be executed with the --no-cache&#x3D;true flag | [optional] 
**pull_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


