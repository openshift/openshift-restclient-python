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


class V1beta1PodSecurityPolicySpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, allowed_capabilities=None, default_add_capabilities=None, fs_group=None, host_ipc=None, host_network=None, host_pid=None, host_ports=None, privileged=None, read_only_root_filesystem=None, required_drop_capabilities=None, run_as_user=None, se_linux=None, supplemental_groups=None, volumes=None):
        """
        V1beta1PodSecurityPolicySpec - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'allowed_capabilities': 'list[str]',
            'default_add_capabilities': 'list[str]',
            'fs_group': 'V1beta1FSGroupStrategyOptions',
            'host_ipc': 'bool',
            'host_network': 'bool',
            'host_pid': 'bool',
            'host_ports': 'list[V1beta1HostPortRange]',
            'privileged': 'bool',
            'read_only_root_filesystem': 'bool',
            'required_drop_capabilities': 'list[str]',
            'run_as_user': 'V1beta1RunAsUserStrategyOptions',
            'se_linux': 'V1beta1SELinuxStrategyOptions',
            'supplemental_groups': 'V1beta1SupplementalGroupsStrategyOptions',
            'volumes': 'list[str]'
        }

        self.attribute_map = {
            'allowed_capabilities': 'allowedCapabilities',
            'default_add_capabilities': 'defaultAddCapabilities',
            'fs_group': 'fsGroup',
            'host_ipc': 'hostIPC',
            'host_network': 'hostNetwork',
            'host_pid': 'hostPID',
            'host_ports': 'hostPorts',
            'privileged': 'privileged',
            'read_only_root_filesystem': 'readOnlyRootFilesystem',
            'required_drop_capabilities': 'requiredDropCapabilities',
            'run_as_user': 'runAsUser',
            'se_linux': 'seLinux',
            'supplemental_groups': 'supplementalGroups',
            'volumes': 'volumes'
        }

        self._allowed_capabilities = allowed_capabilities
        self._default_add_capabilities = default_add_capabilities
        self._fs_group = fs_group
        self._host_ipc = host_ipc
        self._host_network = host_network
        self._host_pid = host_pid
        self._host_ports = host_ports
        self._privileged = privileged
        self._read_only_root_filesystem = read_only_root_filesystem
        self._required_drop_capabilities = required_drop_capabilities
        self._run_as_user = run_as_user
        self._se_linux = se_linux
        self._supplemental_groups = supplemental_groups
        self._volumes = volumes

    @property
    def allowed_capabilities(self):
        """
        Gets the allowed_capabilities of this V1beta1PodSecurityPolicySpec.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :return: The allowed_capabilities of this V1beta1PodSecurityPolicySpec.
        :rtype: list[str]
        """
        return self._allowed_capabilities

    @allowed_capabilities.setter
    def allowed_capabilities(self, allowed_capabilities):
        """
        Sets the allowed_capabilities of this V1beta1PodSecurityPolicySpec.
        AllowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both AllowedCapabilities and RequiredDropCapabilities.

        :param allowed_capabilities: The allowed_capabilities of this V1beta1PodSecurityPolicySpec.
        :type: list[str]
        """

        self._allowed_capabilities = allowed_capabilities

    @property
    def default_add_capabilities(self):
        """
        Gets the default_add_capabilities of this V1beta1PodSecurityPolicySpec.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :return: The default_add_capabilities of this V1beta1PodSecurityPolicySpec.
        :rtype: list[str]
        """
        return self._default_add_capabilities

    @default_add_capabilities.setter
    def default_add_capabilities(self, default_add_capabilities):
        """
        Sets the default_add_capabilities of this V1beta1PodSecurityPolicySpec.
        DefaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.  You may not list a capabiility in both DefaultAddCapabilities and RequiredDropCapabilities.

        :param default_add_capabilities: The default_add_capabilities of this V1beta1PodSecurityPolicySpec.
        :type: list[str]
        """

        self._default_add_capabilities = default_add_capabilities

    @property
    def fs_group(self):
        """
        Gets the fs_group of this V1beta1PodSecurityPolicySpec.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :return: The fs_group of this V1beta1PodSecurityPolicySpec.
        :rtype: V1beta1FSGroupStrategyOptions
        """
        return self._fs_group

    @fs_group.setter
    def fs_group(self, fs_group):
        """
        Sets the fs_group of this V1beta1PodSecurityPolicySpec.
        FSGroup is the strategy that will dictate what fs group is used by the SecurityContext.

        :param fs_group: The fs_group of this V1beta1PodSecurityPolicySpec.
        :type: V1beta1FSGroupStrategyOptions
        """
        if fs_group is None:
            raise ValueError("Invalid value for `fs_group`, must not be `None`")

        self._fs_group = fs_group

    @property
    def host_ipc(self):
        """
        Gets the host_ipc of this V1beta1PodSecurityPolicySpec.
        hostIPC determines if the policy allows the use of HostIPC in the pod spec.

        :return: The host_ipc of this V1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_ipc

    @host_ipc.setter
    def host_ipc(self, host_ipc):
        """
        Sets the host_ipc of this V1beta1PodSecurityPolicySpec.
        hostIPC determines if the policy allows the use of HostIPC in the pod spec.

        :param host_ipc: The host_ipc of this V1beta1PodSecurityPolicySpec.
        :type: bool
        """

        self._host_ipc = host_ipc

    @property
    def host_network(self):
        """
        Gets the host_network of this V1beta1PodSecurityPolicySpec.
        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :return: The host_network of this V1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_network

    @host_network.setter
    def host_network(self, host_network):
        """
        Sets the host_network of this V1beta1PodSecurityPolicySpec.
        hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        :param host_network: The host_network of this V1beta1PodSecurityPolicySpec.
        :type: bool
        """

        self._host_network = host_network

    @property
    def host_pid(self):
        """
        Gets the host_pid of this V1beta1PodSecurityPolicySpec.
        hostPID determines if the policy allows the use of HostPID in the pod spec.

        :return: The host_pid of this V1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._host_pid

    @host_pid.setter
    def host_pid(self, host_pid):
        """
        Sets the host_pid of this V1beta1PodSecurityPolicySpec.
        hostPID determines if the policy allows the use of HostPID in the pod spec.

        :param host_pid: The host_pid of this V1beta1PodSecurityPolicySpec.
        :type: bool
        """

        self._host_pid = host_pid

    @property
    def host_ports(self):
        """
        Gets the host_ports of this V1beta1PodSecurityPolicySpec.
        hostPorts determines which host port ranges are allowed to be exposed.

        :return: The host_ports of this V1beta1PodSecurityPolicySpec.
        :rtype: list[V1beta1HostPortRange]
        """
        return self._host_ports

    @host_ports.setter
    def host_ports(self, host_ports):
        """
        Sets the host_ports of this V1beta1PodSecurityPolicySpec.
        hostPorts determines which host port ranges are allowed to be exposed.

        :param host_ports: The host_ports of this V1beta1PodSecurityPolicySpec.
        :type: list[V1beta1HostPortRange]
        """

        self._host_ports = host_ports

    @property
    def privileged(self):
        """
        Gets the privileged of this V1beta1PodSecurityPolicySpec.
        privileged determines if a pod can request to be run as privileged.

        :return: The privileged of this V1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._privileged

    @privileged.setter
    def privileged(self, privileged):
        """
        Sets the privileged of this V1beta1PodSecurityPolicySpec.
        privileged determines if a pod can request to be run as privileged.

        :param privileged: The privileged of this V1beta1PodSecurityPolicySpec.
        :type: bool
        """

        self._privileged = privileged

    @property
    def read_only_root_filesystem(self):
        """
        Gets the read_only_root_filesystem of this V1beta1PodSecurityPolicySpec.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :return: The read_only_root_filesystem of this V1beta1PodSecurityPolicySpec.
        :rtype: bool
        """
        return self._read_only_root_filesystem

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(self, read_only_root_filesystem):
        """
        Sets the read_only_root_filesystem of this V1beta1PodSecurityPolicySpec.
        ReadOnlyRootFilesystem when set to true will force containers to run with a read only root file system.  If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        :param read_only_root_filesystem: The read_only_root_filesystem of this V1beta1PodSecurityPolicySpec.
        :type: bool
        """

        self._read_only_root_filesystem = read_only_root_filesystem

    @property
    def required_drop_capabilities(self):
        """
        Gets the required_drop_capabilities of this V1beta1PodSecurityPolicySpec.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :return: The required_drop_capabilities of this V1beta1PodSecurityPolicySpec.
        :rtype: list[str]
        """
        return self._required_drop_capabilities

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, required_drop_capabilities):
        """
        Sets the required_drop_capabilities of this V1beta1PodSecurityPolicySpec.
        RequiredDropCapabilities are the capabilities that will be dropped from the container.  These are required to be dropped and cannot be added.

        :param required_drop_capabilities: The required_drop_capabilities of this V1beta1PodSecurityPolicySpec.
        :type: list[str]
        """

        self._required_drop_capabilities = required_drop_capabilities

    @property
    def run_as_user(self):
        """
        Gets the run_as_user of this V1beta1PodSecurityPolicySpec.
        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.

        :return: The run_as_user of this V1beta1PodSecurityPolicySpec.
        :rtype: V1beta1RunAsUserStrategyOptions
        """
        return self._run_as_user

    @run_as_user.setter
    def run_as_user(self, run_as_user):
        """
        Sets the run_as_user of this V1beta1PodSecurityPolicySpec.
        runAsUser is the strategy that will dictate the allowable RunAsUser values that may be set.

        :param run_as_user: The run_as_user of this V1beta1PodSecurityPolicySpec.
        :type: V1beta1RunAsUserStrategyOptions
        """
        if run_as_user is None:
            raise ValueError("Invalid value for `run_as_user`, must not be `None`")

        self._run_as_user = run_as_user

    @property
    def se_linux(self):
        """
        Gets the se_linux of this V1beta1PodSecurityPolicySpec.
        seLinux is the strategy that will dictate the allowable labels that may be set.

        :return: The se_linux of this V1beta1PodSecurityPolicySpec.
        :rtype: V1beta1SELinuxStrategyOptions
        """
        return self._se_linux

    @se_linux.setter
    def se_linux(self, se_linux):
        """
        Sets the se_linux of this V1beta1PodSecurityPolicySpec.
        seLinux is the strategy that will dictate the allowable labels that may be set.

        :param se_linux: The se_linux of this V1beta1PodSecurityPolicySpec.
        :type: V1beta1SELinuxStrategyOptions
        """
        if se_linux is None:
            raise ValueError("Invalid value for `se_linux`, must not be `None`")

        self._se_linux = se_linux

    @property
    def supplemental_groups(self):
        """
        Gets the supplemental_groups of this V1beta1PodSecurityPolicySpec.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :return: The supplemental_groups of this V1beta1PodSecurityPolicySpec.
        :rtype: V1beta1SupplementalGroupsStrategyOptions
        """
        return self._supplemental_groups

    @supplemental_groups.setter
    def supplemental_groups(self, supplemental_groups):
        """
        Sets the supplemental_groups of this V1beta1PodSecurityPolicySpec.
        SupplementalGroups is the strategy that will dictate what supplemental groups are used by the SecurityContext.

        :param supplemental_groups: The supplemental_groups of this V1beta1PodSecurityPolicySpec.
        :type: V1beta1SupplementalGroupsStrategyOptions
        """
        if supplemental_groups is None:
            raise ValueError("Invalid value for `supplemental_groups`, must not be `None`")

        self._supplemental_groups = supplemental_groups

    @property
    def volumes(self):
        """
        Gets the volumes of this V1beta1PodSecurityPolicySpec.
        volumes is a white list of allowed volume plugins.  Empty indicates that all plugins may be used.

        :return: The volumes of this V1beta1PodSecurityPolicySpec.
        :rtype: list[str]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1beta1PodSecurityPolicySpec.
        volumes is a white list of allowed volume plugins.  Empty indicates that all plugins may be used.

        :param volumes: The volumes of this V1beta1PodSecurityPolicySpec.
        :type: list[str]
        """

        self._volumes = volumes

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
        if not isinstance(other, V1beta1PodSecurityPolicySpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
