# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a client. By listing and beginning a watch from the returned resourceVersion, clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: v3.6.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1Image(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, api_version=None, docker_image_config=None, docker_image_layers=None, docker_image_manifest=None, docker_image_manifest_media_type=None, docker_image_metadata=None, docker_image_metadata_version=None, docker_image_reference=None, docker_image_signatures=None, kind=None, metadata=None, signatures=None):
        """
        V1Image - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'api_version': 'str',
            'docker_image_config': 'str',
            'docker_image_layers': 'list[V1ImageLayer]',
            'docker_image_manifest': 'str',
            'docker_image_manifest_media_type': 'str',
            'docker_image_metadata': 'RuntimeRawExtension',
            'docker_image_metadata_version': 'str',
            'docker_image_reference': 'str',
            'docker_image_signatures': 'list[str]',
            'kind': 'str',
            'metadata': 'V1ObjectMeta',
            'signatures': 'list[V1ImageSignature]'
        }

        self.attribute_map = {
            'api_version': 'apiVersion',
            'docker_image_config': 'dockerImageConfig',
            'docker_image_layers': 'dockerImageLayers',
            'docker_image_manifest': 'dockerImageManifest',
            'docker_image_manifest_media_type': 'dockerImageManifestMediaType',
            'docker_image_metadata': 'dockerImageMetadata',
            'docker_image_metadata_version': 'dockerImageMetadataVersion',
            'docker_image_reference': 'dockerImageReference',
            'docker_image_signatures': 'dockerImageSignatures',
            'kind': 'kind',
            'metadata': 'metadata',
            'signatures': 'signatures'
        }

        self._api_version = api_version
        self._docker_image_config = docker_image_config
        self._docker_image_layers = docker_image_layers
        self._docker_image_manifest = docker_image_manifest
        self._docker_image_manifest_media_type = docker_image_manifest_media_type
        self._docker_image_metadata = docker_image_metadata
        self._docker_image_metadata_version = docker_image_metadata_version
        self._docker_image_reference = docker_image_reference
        self._docker_image_signatures = docker_image_signatures
        self._kind = kind
        self._metadata = metadata
        self._signatures = signatures

    @property
    def api_version(self):
        """
        Gets the api_version of this V1Image.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :return: The api_version of this V1Image.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1Image.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#resources

        :param api_version: The api_version of this V1Image.
        :type: str
        """

        self._api_version = api_version

    @property
    def docker_image_config(self):
        """
        Gets the docker_image_config of this V1Image.
        DockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2.

        :return: The docker_image_config of this V1Image.
        :rtype: str
        """
        return self._docker_image_config

    @docker_image_config.setter
    def docker_image_config(self, docker_image_config):
        """
        Sets the docker_image_config of this V1Image.
        DockerImageConfig is a JSON blob that the runtime uses to set up the container. This is a part of manifest schema v2.

        :param docker_image_config: The docker_image_config of this V1Image.
        :type: str
        """

        self._docker_image_config = docker_image_config

    @property
    def docker_image_layers(self):
        """
        Gets the docker_image_layers of this V1Image.
        DockerImageLayers represents the layers in the image. May not be set if the image does not define that data.

        :return: The docker_image_layers of this V1Image.
        :rtype: list[V1ImageLayer]
        """
        return self._docker_image_layers

    @docker_image_layers.setter
    def docker_image_layers(self, docker_image_layers):
        """
        Sets the docker_image_layers of this V1Image.
        DockerImageLayers represents the layers in the image. May not be set if the image does not define that data.

        :param docker_image_layers: The docker_image_layers of this V1Image.
        :type: list[V1ImageLayer]
        """
        if docker_image_layers is None:
            raise ValueError("Invalid value for `docker_image_layers`, must not be `None`")

        self._docker_image_layers = docker_image_layers

    @property
    def docker_image_manifest(self):
        """
        Gets the docker_image_manifest of this V1Image.
        DockerImageManifest is the raw JSON of the manifest

        :return: The docker_image_manifest of this V1Image.
        :rtype: str
        """
        return self._docker_image_manifest

    @docker_image_manifest.setter
    def docker_image_manifest(self, docker_image_manifest):
        """
        Sets the docker_image_manifest of this V1Image.
        DockerImageManifest is the raw JSON of the manifest

        :param docker_image_manifest: The docker_image_manifest of this V1Image.
        :type: str
        """

        self._docker_image_manifest = docker_image_manifest

    @property
    def docker_image_manifest_media_type(self):
        """
        Gets the docker_image_manifest_media_type of this V1Image.
        DockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.

        :return: The docker_image_manifest_media_type of this V1Image.
        :rtype: str
        """
        return self._docker_image_manifest_media_type

    @docker_image_manifest_media_type.setter
    def docker_image_manifest_media_type(self, docker_image_manifest_media_type):
        """
        Sets the docker_image_manifest_media_type of this V1Image.
        DockerImageManifestMediaType specifies the mediaType of manifest. This is a part of manifest schema v2.

        :param docker_image_manifest_media_type: The docker_image_manifest_media_type of this V1Image.
        :type: str
        """

        self._docker_image_manifest_media_type = docker_image_manifest_media_type

    @property
    def docker_image_metadata(self):
        """
        Gets the docker_image_metadata of this V1Image.
        DockerImageMetadata contains metadata about this image

        :return: The docker_image_metadata of this V1Image.
        :rtype: RuntimeRawExtension
        """
        return self._docker_image_metadata

    @docker_image_metadata.setter
    def docker_image_metadata(self, docker_image_metadata):
        """
        Sets the docker_image_metadata of this V1Image.
        DockerImageMetadata contains metadata about this image

        :param docker_image_metadata: The docker_image_metadata of this V1Image.
        :type: RuntimeRawExtension
        """

        self._docker_image_metadata = docker_image_metadata

    @property
    def docker_image_metadata_version(self):
        """
        Gets the docker_image_metadata_version of this V1Image.
        DockerImageMetadataVersion conveys the version of the object, which if empty defaults to \"1.0\"

        :return: The docker_image_metadata_version of this V1Image.
        :rtype: str
        """
        return self._docker_image_metadata_version

    @docker_image_metadata_version.setter
    def docker_image_metadata_version(self, docker_image_metadata_version):
        """
        Sets the docker_image_metadata_version of this V1Image.
        DockerImageMetadataVersion conveys the version of the object, which if empty defaults to \"1.0\"

        :param docker_image_metadata_version: The docker_image_metadata_version of this V1Image.
        :type: str
        """

        self._docker_image_metadata_version = docker_image_metadata_version

    @property
    def docker_image_reference(self):
        """
        Gets the docker_image_reference of this V1Image.
        DockerImageReference is the string that can be used to pull this image.

        :return: The docker_image_reference of this V1Image.
        :rtype: str
        """
        return self._docker_image_reference

    @docker_image_reference.setter
    def docker_image_reference(self, docker_image_reference):
        """
        Sets the docker_image_reference of this V1Image.
        DockerImageReference is the string that can be used to pull this image.

        :param docker_image_reference: The docker_image_reference of this V1Image.
        :type: str
        """

        self._docker_image_reference = docker_image_reference

    @property
    def docker_image_signatures(self):
        """
        Gets the docker_image_signatures of this V1Image.
        DockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.

        :return: The docker_image_signatures of this V1Image.
        :rtype: list[str]
        """
        return self._docker_image_signatures

    @docker_image_signatures.setter
    def docker_image_signatures(self, docker_image_signatures):
        """
        Sets the docker_image_signatures of this V1Image.
        DockerImageSignatures provides the signatures as opaque blobs. This is a part of manifest schema v1.

        :param docker_image_signatures: The docker_image_signatures of this V1Image.
        :type: list[str]
        """

        self._docker_image_signatures = docker_image_signatures

    @property
    def kind(self):
        """
        Gets the kind of this V1Image.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1Image.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1Image.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1Image.
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """
        Gets the metadata of this V1Image.
        Standard object's metadata.

        :return: The metadata of this V1Image.
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this V1Image.
        Standard object's metadata.

        :param metadata: The metadata of this V1Image.
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def signatures(self):
        """
        Gets the signatures of this V1Image.
        Signatures holds all signatures of the image.

        :return: The signatures of this V1Image.
        :rtype: list[V1ImageSignature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this V1Image.
        Signatures holds all signatures of the image.

        :param signatures: The signatures of this V1Image.
        :type: list[V1ImageSignature]
        """

        self._signatures = signatures

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1Image):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
