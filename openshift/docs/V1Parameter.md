# V1Parameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of a parameter. Optional. | [optional] 
**display_name** | **str** | Optional: The name that will show in UI instead of parameter &#39;Name&#39; | [optional] 
**_from** | **str** | From is an input value for the generator. Optional. | [optional] 
**generate** | **str** | generate specifies the generator to be used to generate random string from an input value specified by From field. The result string is stored into Value field. If empty, no generator is being used, leaving the result Value untouched. Optional.  The only supported generator is \&quot;expression\&quot;, which accepts a \&quot;from\&quot; value in the form of a simple regular expression containing the range expression \&quot;[a-zA-Z0-9]\&quot;, and the length expression \&quot;a{length}\&quot;.  Examples:  from             | value ----------------------------- \&quot;test[0-9]{1}x\&quot;  | \&quot;test7x\&quot; \&quot;[0-1]{8}\&quot;       | \&quot;01001100\&quot; \&quot;0x[A-F0-9]{4}\&quot;  | \&quot;0xB3AF\&quot; \&quot;[a-zA-Z0-9]{8}\&quot; | \&quot;hW4yQU5i\&quot; | [optional] 
**name** | **str** | Name must be set and it can be referenced in Template Items using ${PARAMETER_NAME}. Required. | 
**required** | **bool** | Optional: Indicates the parameter must have a value.  Defaults to false. | [optional] 
**value** | **str** | Value holds the Parameter data. If specified, the generator will be ignored. The value replaces all occurrences of the Parameter ${Name} expression during the Template to Config transformation. Optional. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


