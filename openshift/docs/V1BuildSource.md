# V1BuildSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**binary** | [**V1BinaryBuildSource**](V1BinaryBuildSource.md) | binary builds accept a binary as their input. The binary is generally assumed to be a tar, gzipped tar, or zip file depending on the strategy. For Docker builds, this is the build context and an optional Dockerfile may be specified to override any Dockerfile in the build context. For Source builds, this is assumed to be an archive as described above. For Source and Docker builds, if binary.asFile is set the build will receive a directory with a single file. contextDir may be used when an archive is provided. Custom builds will receive this binary as input on STDIN. | [optional] 
**context_dir** | **str** | contextDir specifies the sub-directory where the source code for the application exists. This allows to have buildable sources in directory other than root of repository. | [optional] 
**dockerfile** | **str** | dockerfile is the raw contents of a Dockerfile which should be built. When this option is specified, the FROM may be modified based on your strategy base image and additional ENV stanzas from your strategy environment will be added after the FROM, but before the rest of your Dockerfile stanzas. The Dockerfile source type may be used with other options like git - in those cases the Git repo will have any innate Dockerfile replaced in the context dir. | [optional] 
**git** | [**V1GitBuildSource**](V1GitBuildSource.md) | git contains optional information about git build source | [optional] 
**images** | [**list[V1ImageSource]**](V1ImageSource.md) | images describes a set of images to be used to provide source for the build | [optional] 
**secrets** | [**list[V1SecretBuildSource]**](V1SecretBuildSource.md) | secrets represents a list of secrets and their destinations that will be used only for the build. | [optional] 
**source_secret** | [**V1LocalObjectReference**](V1LocalObjectReference.md) | sourceSecret is the name of a Secret that would be used for setting up the authentication for cloning private repository. The secret contains valid credentials for remote repository, where the data&#39;s key represent the authentication method to be used and value is the base64 encoded credentials. Supported auth methods are: ssh-privatekey. | [optional] 
**type** | **str** | type of build input to accept | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


