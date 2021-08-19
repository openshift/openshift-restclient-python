from kubernetes.dynamic.exceptions import *  # noqa


class ApplyException(Exception):
    """ Could not apply patch """
