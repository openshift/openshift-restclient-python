# V1ImageSignature

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources | [optional] 
**conditions** | [**list[V1SignatureCondition]**](V1SignatureCondition.md) | Conditions represent the latest available observations of a signature&#39;s current state. | [optional] 
**content** | **str** | Required: An opaque binary string which is an image&#39;s signature. | 
**created** | [**UnversionedTime**](UnversionedTime.md) | If specified, it is the time of signature&#39;s creation. | [optional] 
**image_identity** | **str** | A human readable string representing image&#39;s identity. It could be a product name and version, or an image pull spec (e.g. \&quot;registry.access.redhat.com/rhel7/rhel:7.2\&quot;). | [optional] 
**issued_by** | [**V1SignatureIssuer**](V1SignatureIssuer.md) | If specified, it holds information about an issuer of signing certificate or key (a person or entity who signed the signing certificate or key). | [optional] 
**issued_to** | [**V1SignatureSubject**](V1SignatureSubject.md) | If specified, it holds information about a subject of signing certificate or key (a person or entity who signed the image). | [optional] 
**kind** | **str** | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the openshift.client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds | [optional] 
**metadata** | [**V1ObjectMeta**](V1ObjectMeta.md) | Standard object&#39;s metadata. | [optional] 
**signed_claims** | **dict(str, str)** | Contains claims from the signature. | [optional] 
**type** | **str** | Required: Describes a type of stored blob. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


