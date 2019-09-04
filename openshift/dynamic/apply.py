from copy import deepcopy
import json

from openshift.dynamic.exceptions import NotFoundError

LAST_APPLIED_CONFIG_ANNOTATION = 'kubectl.kubernetes.io/last-applied-configuration'

def apply_object(resource, definition):
    desired_annotation = dict(
        metadata=dict(
            annotations={
                LAST_APPLIED_CONFIG_ANNOTATION: json.dumps(definition, separators=(',', ':'), indent=None)
            }
        )
    )
    try:
        actual = resource.get(name=definition['metadata']['name'], namespace=definition['metadata'].get('namespace'))
    except NotFoundError:
        return None, dict_merge(definition, desired_annotation)
    last_applied = actual.metadata.get('annotations',{}).get(LAST_APPLIED_CONFIG_ANNOTATION)

    if last_applied:
        last_applied = json.loads(last_applied)
        actual_dict = actual.to_dict()
        del actual_dict['metadata']['annotations'][LAST_APPLIED_CONFIG_ANNOTATION]
        patch = merge(last_applied, definition, actual_dict)
        if patch:
            return actual.to_dict(), dict_merge(patch, desired_annotation)
        else:
            return actual.to_dict(), actual.to_dict()
    else:
        return actual.to_dict(), dict_merge(definition, desired_annotation)


def apply(resource, definition):
    existing, desired = apply_object(resource, definition)
    if not existing:
        return resource.create(body=desired, namespace=definition['metadata'].get('namespace'))
    if existing == desired:
        return resource.get(name=definition['metadata']['name'], namespace=definition['metadata'].get('namespace'))
    return resource.patch(body=desired,
                          name=definition['metadata']['name'],
                          namespace=definition['metadata'].get('namespace'),
                          content_type='application/merge-patch+json')


# The patch is the difference from actual to desired without deletions, plus deletions
# from last_applied to desired. To find it, we compute deletions, which are the deletions from
# last_applied to desired, and delta, which is the difference from actual to desired without
# deletions, and then apply delta to deletions as a patch, which should be strictly additive.
def merge(last_applied, desired, actual):
    deletions = get_deletions(last_applied, desired)
    delta = get_delta(actual, desired)
    return dict_merge(deletions, delta)


# dict_merge taken from Ansible's module_utils.common.dict_transformations
def dict_merge(a, b):
    '''recursively merges dicts. not just simple a['key'] = b['key'], if
    both a and b have a key whose value is a dict then dict_merge is called
    on both values and the result stored in the returned dictionary.'''
    if not isinstance(b, dict):
        return b
    result = deepcopy(a)
    for k, v in b.items():
        if k in result and isinstance(result[k], dict):
            result[k] = dict_merge(result[k], v)
        else:
            result[k] = deepcopy(v)
    return result


def get_deletions(last_applied, desired):
    patch = {}
    for k, last_applied_value in last_applied.items():
        desired_value = desired.get(k)
        if isinstance(last_applied_value, dict) and isinstance(desired_value, dict):
            p = get_deletions(last_applied_value, desired_value)
            if p:
                patch[k] = p
        elif last_applied_value != desired_value:
            patch[k] = desired_value
    return patch


def get_delta(actual, desired):
    patch = {}
    for k, desired_value in desired.items():
        actual_value = actual.get(k)
        if actual_value is None:
            patch[k] = desired_value
        elif isinstance(desired_value, dict):
            p = get_delta(actual_value, desired_value)
            if p:
                patch[k] = p
    return patch
