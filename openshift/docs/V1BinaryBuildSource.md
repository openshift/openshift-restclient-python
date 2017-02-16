# V1BinaryBuildSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_file** | **str** | asFile indicates that the provided binary input should be considered a single file within the build input. For example, specifying \&quot;webapp.war\&quot; would place the provided binary as &#x60;/webapp.war&#x60; for the builder. If left empty, the Docker and Source build strategies assume this file is a zip, tar, or tar.gz file and extract it as the source. The custom strategy receives this binary as standard input. This filename may not contain slashes or be &#39;..&#39; or &#39;.&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


