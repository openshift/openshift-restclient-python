import yaml

from openshift.dynamic.exceptions import NotFoundError

LAST_APPLIED_CONFIG_ANNOTATION = 'kubectl.kubernetes.io/last-applied-configuration'

def apply(resource, definition):
    definition['metadata']['annotations'][LAST_APPLIED_CONFIG_ANNOTATION] = definition
    try:
        actual = resource.get(name=definition['metadata']['name'], namespace=definition['metadata']['namespace']).to_dict()
    except NotFoundError:
        return resource.create(body=definition)
    last_applied = actual['metadata']['annotations'].get(LAST_APPLIED_CONFIG_ANNOTATION)
    if last_applied:
        last_applied = yaml.load(last_applied)
        del actual['metadata']['annotations'][LAST_APPLIED_CONFIG_ANNOTATION]
    else:
        return resource.patch(body=definition, name=definition['metadata']['name'], namespace=definition['metadata']['namespace'])

    patch = merge(last_applied, definition, actual)
    if patch:
        return resource.patch(body=patch, name=definition['metadata']['name'], namespace=definition['metadata']['namespace'])
    else:
        return "No update necessary"


# The patch is the difference from actual to desired without deletions, plus deletions
# from last_applied to desired. To find it, we compute deletions, which are the deletions from
# last_applied to desired, and delta, which is the difference from actual to desired without
# deletions, and then apply delta to deletions as a patch, which should be strictly additive.
def merge(last_applied, desired, actual):
    base = {}
    deletions = get_deletions(last_applied, desired)
    delta = get_delta(actual, desired)
    base.update(deletions)
    base.update(delta)
    return base


def get_deletions(last_applied, desired):
    patch = {}
    for k, last_applied_value in last_applied.items():
        desired_value = desired.get(k)
        if desired_value is None:
            patch[k] = None
            continue
        if type(last_applied_value) != type(desired_value):
            continue
        if isinstance(last_applied_value, dict):
            p = get_deletions(last_applied_value, desired_value)
            if p:
                patch[k] = p
        elif isinstance(last_applied_value, (list, tuple)):
            # I have no idea what to do here
            pass
    return patch


def get_delta(actual, desired):
    patch = {}
    for k, desired_value in desired.items():
        actual_value = actual.get(k)
        if actual_value is None:
            patch[k] = desired_value
            continue
        if desired_value == actual_value:
            continue
        if type(desired_value) != type(actual_value):
            patch[k] = desired_value
        elif isinstance(desired_value, dict):
            p = get_delta(actual_value, desired_value)
            if p:
                patch[k] = p
        elif isinstance(actual_value, (list, tuple)):
            # I have no idea what to do here
            patch[k] = desired_value
        else:
            patch[k] = desired_value
    return patch
