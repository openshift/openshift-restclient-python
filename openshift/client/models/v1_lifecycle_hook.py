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


class V1LifecycleHook(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, exec_new_pod=None, failure_policy=None, tag_images=None):
        """
        V1LifecycleHook - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'exec_new_pod': 'V1ExecNewPodHook',
            'failure_policy': 'str',
            'tag_images': 'list[V1TagImageHook]'
        }

        self.attribute_map = {
            'exec_new_pod': 'execNewPod',
            'failure_policy': 'failurePolicy',
            'tag_images': 'tagImages'
        }

        self._exec_new_pod = exec_new_pod
        self._failure_policy = failure_policy
        self._tag_images = tag_images

    @property
    def exec_new_pod(self):
        """
        Gets the exec_new_pod of this V1LifecycleHook.
        ExecNewPod specifies the options for a lifecycle hook backed by a pod.

        :return: The exec_new_pod of this V1LifecycleHook.
        :rtype: V1ExecNewPodHook
        """
        return self._exec_new_pod

    @exec_new_pod.setter
    def exec_new_pod(self, exec_new_pod):
        """
        Sets the exec_new_pod of this V1LifecycleHook.
        ExecNewPod specifies the options for a lifecycle hook backed by a pod.

        :param exec_new_pod: The exec_new_pod of this V1LifecycleHook.
        :type: V1ExecNewPodHook
        """

        self._exec_new_pod = exec_new_pod

    @property
    def failure_policy(self):
        """
        Gets the failure_policy of this V1LifecycleHook.
        FailurePolicy specifies what action to take if the hook fails.

        :return: The failure_policy of this V1LifecycleHook.
        :rtype: str
        """
        return self._failure_policy

    @failure_policy.setter
    def failure_policy(self, failure_policy):
        """
        Sets the failure_policy of this V1LifecycleHook.
        FailurePolicy specifies what action to take if the hook fails.

        :param failure_policy: The failure_policy of this V1LifecycleHook.
        :type: str
        """
        if failure_policy is None:
            raise ValueError("Invalid value for `failure_policy`, must not be `None`")

        self._failure_policy = failure_policy

    @property
    def tag_images(self):
        """
        Gets the tag_images of this V1LifecycleHook.
        TagImages instructs the deployer to tag the current image referenced under a container onto an image stream tag.

        :return: The tag_images of this V1LifecycleHook.
        :rtype: list[V1TagImageHook]
        """
        return self._tag_images

    @tag_images.setter
    def tag_images(self, tag_images):
        """
        Sets the tag_images of this V1LifecycleHook.
        TagImages instructs the deployer to tag the current image referenced under a container onto an image stream tag.

        :param tag_images: The tag_images of this V1LifecycleHook.
        :type: list[V1TagImageHook]
        """

        self._tag_images = tag_images

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
        if not isinstance(other, V1LifecycleHook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
