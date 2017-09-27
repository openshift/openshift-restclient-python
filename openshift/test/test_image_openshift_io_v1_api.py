# coding: utf-8

"""
    OpenShift API (with Kubernetes)

    OpenShift provides builds, application lifecycle, image content management, and administrative policy on top of Kubernetes. The API allows consistent management of those objects.  All API operations are authenticated via an Authorization bearer token that is provided for service accounts as a generated secret (in JWT form) or via the native OAuth endpoint located at /oauth/authorize. Core infrastructure components may use openshift.client certificates that require no authentication.  All API operations return a 'resourceVersion' string that represents the version of the object in the underlying storage. The standard LIST operation performs a snapshot read of the underlying objects, returning a resourceVersion representing a consistent version of the listed objects. The WATCH operation allows all updates to a set of objects after the provided resourceVersion to be observed by a openshift.client. By listing and beginning a watch from the returned resourceVersion, openshift.clients may observe a consistent view of the state of one or more objects. Note that WATCH always returns the update after the provided resourceVersion. Watch may be extended a limited time in the past - using etcd 2 the watch window is 1000 events (which on a large cluster may only be a few tens of seconds) so openshift.clients must explicitly handle the \"watch to old error\" by re-listing.  Objects are divided into two rough categories - those that have a lifecycle and must reflect the state of the cluster, and those that have no state. Objects with lifecycle typically have three main sections:  * 'metadata' common to all objects * a 'spec' that represents the desired state * a 'status' that represents how much of the desired state is reflected on   the cluster at the current time  Objects that have no state have 'metadata' but may lack a 'spec' or 'status' section.  Objects are divided into those that are namespace scoped (only exist inside of a namespace) and those that are cluster scoped (exist outside of a namespace). A namespace scoped resource will be deleted when the namespace is deleted and cannot be created if the namespace has not yet been created or is in the process of deletion. Cluster scoped resources are typically only accessible to admins - resources like nodes, persistent volumes, and cluster policy.  All objects have a schema that is a combination of the 'kind' and 'apiVersion' fields. This schema is additive only for any given version - no backwards incompatible changes are allowed without incrementing the apiVersion. The server will return and accept a number of standard responses that share a common schema - for instance, the common error type is 'metav1.Status' (described below) and will be returned on any error from the API server.  The API is available in multiple serialization formats - the default is JSON (Accept: application/json and Content-Type: application/json) but openshift.clients may also use YAML (application/yaml) or the native Protobuf schema (application/vnd.kubernetes.protobuf). Note that the format of the WATCH API call is slightly different - for JSON it returns newline delimited objects while for Protobuf it returns length-delimited frames (4 bytes in network-order) that contain a 'versioned.Watch' Protobuf object.  See the OpenShift documentation at https://docs.openshift.org for more information. 

    OpenAPI spec version: latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import openshift.client
from kubernetes.client.rest import ApiException
from openshift.client.apis.image_openshift_io_v1_api import ImageOpenshiftIoV1Api


class TestImageOpenshiftIoV1Api(unittest.TestCase):
    """ ImageOpenshiftIoV1Api unit test stubs """

    def setUp(self):
        self.api = openshift.client.apis.image_openshift_io_v1_api.ImageOpenshiftIoV1Api()

    def tearDown(self):
        pass

    def test_create_image(self):
        """
        Test case for create_image

        
        """
        pass

    def test_create_image_signature(self):
        """
        Test case for create_image_signature

        
        """
        pass

    def test_create_image_stream_for_all_namespaces(self):
        """
        Test case for create_image_stream_for_all_namespaces

        
        """
        pass

    def test_create_image_stream_import_for_all_namespaces(self):
        """
        Test case for create_image_stream_import_for_all_namespaces

        
        """
        pass

    def test_create_image_stream_mapping_for_all_namespaces(self):
        """
        Test case for create_image_stream_mapping_for_all_namespaces

        
        """
        pass

    def test_create_image_stream_tag_for_all_namespaces(self):
        """
        Test case for create_image_stream_tag_for_all_namespaces

        
        """
        pass

    def test_create_namespaced_image_stream(self):
        """
        Test case for create_namespaced_image_stream

        
        """
        pass

    def test_create_namespaced_image_stream_import(self):
        """
        Test case for create_namespaced_image_stream_import

        
        """
        pass

    def test_create_namespaced_image_stream_mapping(self):
        """
        Test case for create_namespaced_image_stream_mapping

        
        """
        pass

    def test_create_namespaced_image_stream_tag(self):
        """
        Test case for create_namespaced_image_stream_tag

        
        """
        pass

    def test_delete_collection_image(self):
        """
        Test case for delete_collection_image

        
        """
        pass

    def test_delete_collection_namespaced_image_stream(self):
        """
        Test case for delete_collection_namespaced_image_stream

        
        """
        pass

    def test_delete_image(self):
        """
        Test case for delete_image

        
        """
        pass

    def test_delete_image_signature(self):
        """
        Test case for delete_image_signature

        
        """
        pass

    def test_delete_namespaced_image_stream(self):
        """
        Test case for delete_namespaced_image_stream

        
        """
        pass

    def test_delete_namespaced_image_stream_tag(self):
        """
        Test case for delete_namespaced_image_stream_tag

        
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        
        """
        pass

    def test_list_image(self):
        """
        Test case for list_image

        
        """
        pass

    def test_list_image_stream_for_all_namespaces(self):
        """
        Test case for list_image_stream_for_all_namespaces

        
        """
        pass

    def test_list_image_stream_tag_for_all_namespaces(self):
        """
        Test case for list_image_stream_tag_for_all_namespaces

        
        """
        pass

    def test_list_namespaced_image_stream(self):
        """
        Test case for list_namespaced_image_stream

        
        """
        pass

    def test_list_namespaced_image_stream_tag(self):
        """
        Test case for list_namespaced_image_stream_tag

        
        """
        pass

    def test_patch_image(self):
        """
        Test case for patch_image

        
        """
        pass

    def test_patch_namespaced_image_stream(self):
        """
        Test case for patch_namespaced_image_stream

        
        """
        pass

    def test_patch_namespaced_image_stream_status(self):
        """
        Test case for patch_namespaced_image_stream_status

        
        """
        pass

    def test_patch_namespaced_image_stream_tag(self):
        """
        Test case for patch_namespaced_image_stream_tag

        
        """
        pass

    def test_read_image(self):
        """
        Test case for read_image

        
        """
        pass

    def test_read_namespaced_image_stream(self):
        """
        Test case for read_namespaced_image_stream

        
        """
        pass

    def test_read_namespaced_image_stream_image(self):
        """
        Test case for read_namespaced_image_stream_image

        
        """
        pass

    def test_read_namespaced_image_stream_status(self):
        """
        Test case for read_namespaced_image_stream_status

        
        """
        pass

    def test_read_namespaced_image_stream_tag(self):
        """
        Test case for read_namespaced_image_stream_tag

        
        """
        pass

    def test_read_namespaced_secret_list_secrets(self):
        """
        Test case for read_namespaced_secret_list_secrets

        
        """
        pass

    def test_replace_image(self):
        """
        Test case for replace_image

        
        """
        pass

    def test_replace_namespaced_image_stream(self):
        """
        Test case for replace_namespaced_image_stream

        
        """
        pass

    def test_replace_namespaced_image_stream_status(self):
        """
        Test case for replace_namespaced_image_stream_status

        
        """
        pass

    def test_replace_namespaced_image_stream_tag(self):
        """
        Test case for replace_namespaced_image_stream_tag

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
