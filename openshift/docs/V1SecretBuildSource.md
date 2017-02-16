# V1SecretBuildSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_dir** | **str** | destinationDir is the directory where the files from the secret should be available for the build time. For the Source build strategy, these will be injected into a container where the assemble script runs. Later, when the script finishes, all files injected will be truncated to zero length. For the Docker build strategy, these will be copied into the build directory, where the Dockerfile is located, so users can ADD or COPY them during docker build. | [optional] 
**secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | secret is a reference to an existing secret that you want to use in your build. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


