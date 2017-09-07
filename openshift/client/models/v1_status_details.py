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


class V1StatusDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, causes=None, group=None, kind=None, name=None, retry_after_seconds=None):
        """
        V1StatusDetails - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'causes': 'list[V1StatusCause]',
            'group': 'str',
            'kind': 'str',
            'name': 'str',
            'retry_after_seconds': 'int'
        }

        self.attribute_map = {
            'causes': 'causes',
            'group': 'group',
            'kind': 'kind',
            'name': 'name',
            'retry_after_seconds': 'retryAfterSeconds'
        }

        self._causes = causes
        self._group = group
        self._kind = kind
        self._name = name
        self._retry_after_seconds = retry_after_seconds

    @property
    def causes(self):
        """
        Gets the causes of this V1StatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :return: The causes of this V1StatusDetails.
        :rtype: list[V1StatusCause]
        """
        return self._causes

    @causes.setter
    def causes(self, causes):
        """
        Sets the causes of this V1StatusDetails.
        The Causes array includes more details associated with the StatusReason failure. Not all StatusReasons may provide detailed causes.

        :param causes: The causes of this V1StatusDetails.
        :type: list[V1StatusCause]
        """

        self._causes = causes

    @property
    def group(self):
        """
        Gets the group of this V1StatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :return: The group of this V1StatusDetails.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """
        Sets the group of this V1StatusDetails.
        The group attribute of the resource associated with the status StatusReason.

        :param group: The group of this V1StatusDetails.
        :type: str
        """

        self._group = group

    @property
    def kind(self):
        """
        Gets the kind of this V1StatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :return: The kind of this V1StatusDetails.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1StatusDetails.
        The kind attribute of the resource associated with the status StatusReason. On some operations may differ from the requested resource Kind. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds

        :param kind: The kind of this V1StatusDetails.
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """
        Gets the name of this V1StatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :return: The name of this V1StatusDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1StatusDetails.
        The name attribute of the resource associated with the status StatusReason (when there is a single name which can be described).

        :param name: The name of this V1StatusDetails.
        :type: str
        """

        self._name = name

    @property
    def retry_after_seconds(self):
        """
        Gets the retry_after_seconds of this V1StatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :return: The retry_after_seconds of this V1StatusDetails.
        :rtype: int
        """
        return self._retry_after_seconds

    @retry_after_seconds.setter
    def retry_after_seconds(self, retry_after_seconds):
        """
        Sets the retry_after_seconds of this V1StatusDetails.
        If specified, the time in seconds before the operation should be retried.

        :param retry_after_seconds: The retry_after_seconds of this V1StatusDetails.
        :type: int
        """

        self._retry_after_seconds = retry_after_seconds

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
        if not isinstance(other, V1StatusDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
