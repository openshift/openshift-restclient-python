# OpenShift User-Password Login helper module
# This module extends the `kubernetes.client.Configuration` object.
# `OCPLoginConfiguration` uses `username` and `password` params to authenticate
# with the OAuth OpenShift component, after the autentication the `api_key` value is set
# with the Bearer token.
#
# IMPORTANT: the Bearer token is designed to expire, si up to the user to renew the token.
# the valitity (in secods) is saved into the `token['expires_in`]` attribute.
# The value refers to when the token has been created and to not change overtime.

# Related discussion on GitHub https://github.com/openshift/openshift-restclient-python/issues/249
# Most part of the code has been taken from the k8s_auth ansible module:
# https://github.com/ansible/ansible/blob/stable-2.9/lib/ansible/modules/clustering/k8s/k8s_auth.py

import requests
from requests_oauthlib import OAuth2Session
from urllib3.util import make_headers
from urllib.parse import parse_qs, urlencode, urlparse
from kubernetes.client import Configuration as KubeConfig

class OCPLoginException(Exception):
    """The base class for the OCPLogin exceptions"""

class OCPLoginRequestException(OCPLoginException):
    def __init__(self, msg, **kwargs):
        self.msg = msg
        self.req_info = {}
        for k, v in kwargs.items():
            self.req_info['req_' + k] = v

    def __str__(self):
        error_msg = self.msg
        for k, v in self.req_info.items():
            error_msg += '\t{0}: {1}\n'.format(k, v)
        return error_msg

class OCPLoginConfiguration(KubeConfig):
    def __init__(self, host="http://localhost",
                 api_key=None, api_key_prefix=None,
                 ocp_username=None, ocp_password=None,
                 discard_unknown_keys=False,
                 ):

        self.ocp_username = ocp_username
        self.ocp_password = ocp_password

        super(OCPLoginConfiguration, self).__init__(host=host, api_key=None,
                api_key_prefix=None, username=None,
                password=None, discard_unknown_keys=discard_unknown_keys)

    def get_token(self):
        # python-requests takes either a bool or a path to a ca file as the 'verify' param
        if self.verify_ssl and self.ssl_ca_cert:
            self.con_verify_ca = self.ssl_ca_cert  # path
        else:
            self.con_verify_ca = self.verify_ssl   # bool

        self.discover()
        self.token = self.login()
        self.api_key = {"authorization": "Bearer " + self.token['access_token']}
        self.api_key_expires = self.token['expires_in']
        self.api_key_scope = self.token['scope']

    def discover(self):
        url = '{0}/.well-known/oauth-authorization-server'.format(self.host)
        ret = requests.get(url, verify=self.con_verify_ca)

        if ret.status_code != 200:
            raise OCPLoginRequestException("Couldn't find OpenShift's OAuth API", method='GET', url=url,
                              reason=ret.reason, status_code=ret.status_code)

        oauth_info = ret.json()
        self.openshift_auth_endpoint = oauth_info['authorization_endpoint']
        self.openshift_token_endpoint = oauth_info['token_endpoint']

    def login(self):
        os_oauth = OAuth2Session(client_id='openshift-challenging-client')
        authorization_url, state = os_oauth.authorization_url(self.openshift_auth_endpoint,
                                                              state="1", code_challenge_method='S256')
        auth_headers = make_headers(basic_auth='{0}:{1}'.format(self.ocp_username, self.ocp_password))
        # Request authorization code using basic auth credentials
        ret = os_oauth.get(
            authorization_url,
            headers={'X-Csrf-Token': state, 'authorization': auth_headers.get('authorization')},
            verify=self.con_verify_ca,
            allow_redirects=False
        )

        if ret.status_code != 302:
            raise OCPLoginRequestException("Authorization failed.", method='GET', url=authorization_url,
                              reason=ret.reason, status_code=ret.status_code)

        qwargs = {}
        for k, v in parse_qs(urlparse(ret.headers['Location']).query).items():
            qwargs[k] = v[0]
        qwargs['grant_type'] = 'authorization_code'

        # Using authorization code given to us in the Location header of the previous request, request a token
        ret = os_oauth.post(
            self.openshift_token_endpoint,
            headers={
                'Accept': 'application/json',
                'Content-Type': 'application/x-www-form-urlencoded',
                # This is just base64 encoded 'openshift-challenging-client:'
                'Authorization': 'Basic b3BlbnNoaWZ0LWNoYWxsZW5naW5nLWNsaWVudDo='
            },

            data=urlencode(qwargs),
            verify=self.con_verify_ca
        )
        if ret.status_code != 200:
            raise OCPLoginRequestException("Failed to obtain an authorization token.", method='POST',
                              url=self.openshift_token_endpoint,
                              reason=ret.reason, status_code=ret.status_code)
        return ret.json()

    def logout(self):
        url = '{0}/apis/oauth.openshift.io/v1/oauthaccesstokens/{1}'.format(self.host, self.api_key)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {0}'.format(self.api_key)
        }
        json = {
            "apiVersion": "oauth.openshift.io/v1",
            "kind": "DeleteOptions"
        }
        requests.delete(url, headers=headers, json=json, verify=self.con_verify_ca)
        # Ignore errors, the token will time out eventually anyway
