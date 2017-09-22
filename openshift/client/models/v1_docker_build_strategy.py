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


class V1DockerBuildStrategy(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, build_args=None, dockerfile_path=None, env=None, force_pull=None, _from=None, image_optimization_policy=None, no_cache=None, pull_secret=None):
        """
        V1DockerBuildStrategy - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'build_args': 'list[V1EnvVar]',
            'dockerfile_path': 'str',
            'env': 'list[V1EnvVar]',
            'force_pull': 'bool',
            '_from': 'V1ObjectReference',
            'image_optimization_policy': 'str',
            'no_cache': 'bool',
            'pull_secret': 'V1LocalObjectReference'
        }

        self.attribute_map = {
            'build_args': 'buildArgs',
            'dockerfile_path': 'dockerfilePath',
            'env': 'env',
            'force_pull': 'forcePull',
            '_from': 'from',
            'image_optimization_policy': 'imageOptimizationPolicy',
            'no_cache': 'noCache',
            'pull_secret': 'pullSecret'
        }

        self._build_args = build_args
        self._dockerfile_path = dockerfile_path
        self._env = env
        self._force_pull = force_pull
        self.__from = _from
        self._image_optimization_policy = image_optimization_policy
        self._no_cache = no_cache
        self._pull_secret = pull_secret

    @property
    def build_args(self):
        """
        Gets the build_args of this V1DockerBuildStrategy.
        buildArgs contains build arguments that will be resolved in the Dockerfile.  See https://docs.docker.com/engine/reference/builder/#/arg for more details.

        :return: The build_args of this V1DockerBuildStrategy.
        :rtype: list[V1EnvVar]
        """
        return self._build_args

    @build_args.setter
    def build_args(self, build_args):
        """
        Sets the build_args of this V1DockerBuildStrategy.
        buildArgs contains build arguments that will be resolved in the Dockerfile.  See https://docs.docker.com/engine/reference/builder/#/arg for more details.

        :param build_args: The build_args of this V1DockerBuildStrategy.
        :type: list[V1EnvVar]
        """

        self._build_args = build_args

    @property
    def dockerfile_path(self):
        """
        Gets the dockerfile_path of this V1DockerBuildStrategy.
        dockerfilePath is the path of the Dockerfile that will be used to build the Docker image, relative to the root of the context (contextDir).

        :return: The dockerfile_path of this V1DockerBuildStrategy.
        :rtype: str
        """
        return self._dockerfile_path

    @dockerfile_path.setter
    def dockerfile_path(self, dockerfile_path):
        """
        Sets the dockerfile_path of this V1DockerBuildStrategy.
        dockerfilePath is the path of the Dockerfile that will be used to build the Docker image, relative to the root of the context (contextDir).

        :param dockerfile_path: The dockerfile_path of this V1DockerBuildStrategy.
        :type: str
        """

        self._dockerfile_path = dockerfile_path

    @property
    def env(self):
        """
        Gets the env of this V1DockerBuildStrategy.
        env contains additional environment variables you want to pass into a builder container.

        :return: The env of this V1DockerBuildStrategy.
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """
        Sets the env of this V1DockerBuildStrategy.
        env contains additional environment variables you want to pass into a builder container.

        :param env: The env of this V1DockerBuildStrategy.
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def force_pull(self):
        """
        Gets the force_pull of this V1DockerBuildStrategy.
        forcePull describes if the builder should pull the images from registry prior to building.

        :return: The force_pull of this V1DockerBuildStrategy.
        :rtype: bool
        """
        return self._force_pull

    @force_pull.setter
    def force_pull(self, force_pull):
        """
        Sets the force_pull of this V1DockerBuildStrategy.
        forcePull describes if the builder should pull the images from registry prior to building.

        :param force_pull: The force_pull of this V1DockerBuildStrategy.
        :type: bool
        """

        self._force_pull = force_pull

    @property
    def _from(self):
        """
        Gets the _from of this V1DockerBuildStrategy.
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled the resulting image will be used in the FROM line of the Dockerfile for this build.

        :return: The _from of this V1DockerBuildStrategy.
        :rtype: V1ObjectReference
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this V1DockerBuildStrategy.
        from is reference to an DockerImage, ImageStreamTag, or ImageStreamImage from which the docker image should be pulled the resulting image will be used in the FROM line of the Dockerfile for this build.

        :param _from: The _from of this V1DockerBuildStrategy.
        :type: V1ObjectReference
        """

        self.__from = _from

    @property
    def image_optimization_policy(self):
        """
        Gets the image_optimization_policy of this V1DockerBuildStrategy.
        imageOptimizationPolicy describes what optimizations the system can use when building images to reduce the final size or time spent building the image. The default policy is 'None' which means the final build image will be equivalent to an image created by the Docker build API. The experimental policy 'SkipLayers' will avoid commiting new layers in between each image step, and will fail if the Dockerfile cannot provide compatibility with the 'None' policy. An additional experimental policy 'SkipLayersAndWarn' is the same as 'SkipLayers' but simply warns if compatibility cannot be preserved.

        :return: The image_optimization_policy of this V1DockerBuildStrategy.
        :rtype: str
        """
        return self._image_optimization_policy

    @image_optimization_policy.setter
    def image_optimization_policy(self, image_optimization_policy):
        """
        Sets the image_optimization_policy of this V1DockerBuildStrategy.
        imageOptimizationPolicy describes what optimizations the system can use when building images to reduce the final size or time spent building the image. The default policy is 'None' which means the final build image will be equivalent to an image created by the Docker build API. The experimental policy 'SkipLayers' will avoid commiting new layers in between each image step, and will fail if the Dockerfile cannot provide compatibility with the 'None' policy. An additional experimental policy 'SkipLayersAndWarn' is the same as 'SkipLayers' but simply warns if compatibility cannot be preserved.

        :param image_optimization_policy: The image_optimization_policy of this V1DockerBuildStrategy.
        :type: str
        """

        self._image_optimization_policy = image_optimization_policy

    @property
    def no_cache(self):
        """
        Gets the no_cache of this V1DockerBuildStrategy.
        noCache if set to true indicates that the docker build must be executed with the --no-cache=true flag

        :return: The no_cache of this V1DockerBuildStrategy.
        :rtype: bool
        """
        return self._no_cache

    @no_cache.setter
    def no_cache(self, no_cache):
        """
        Sets the no_cache of this V1DockerBuildStrategy.
        noCache if set to true indicates that the docker build must be executed with the --no-cache=true flag

        :param no_cache: The no_cache of this V1DockerBuildStrategy.
        :type: bool
        """

        self._no_cache = no_cache

    @property
    def pull_secret(self):
        """
        Gets the pull_secret of this V1DockerBuildStrategy.
        pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :return: The pull_secret of this V1DockerBuildStrategy.
        :rtype: V1LocalObjectReference
        """
        return self._pull_secret

    @pull_secret.setter
    def pull_secret(self, pull_secret):
        """
        Sets the pull_secret of this V1DockerBuildStrategy.
        pullSecret is the name of a Secret that would be used for setting up the authentication for pulling the Docker images from the private Docker registries

        :param pull_secret: The pull_secret of this V1DockerBuildStrategy.
        :type: V1LocalObjectReference
        """

        self._pull_secret = pull_secret

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
        if not isinstance(other, V1DockerBuildStrategy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
