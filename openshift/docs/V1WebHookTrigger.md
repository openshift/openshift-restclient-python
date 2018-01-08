# V1WebHookTrigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_env** | **bool** | allowEnv determines whether the webhook can set environment variables; can only be set to true for GenericWebHook. | [optional] 
**secret** | **str** | secret used to validate requests. Deprecated: use SecretReference instead. | [optional] 
**secret_reference** | [**V1SecretLocalReference**](V1SecretLocalReference.md) | secretReference is a reference to a secret in the same namespace, containing the value to be validated when the webhook is invoked. The secret being referenced must contain a key named \&quot;WebHookSecretKey\&quot;, the value of which will be checked against the value supplied in the webhook invocation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


