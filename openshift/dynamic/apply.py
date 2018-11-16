import yaml

from openshift.dynamic.exceptions import NotFoundError

LAST_APPLIED_CONFIG_ANNOTATION = 'kubectl.kubernetes.io/last-applied-configuration'

def apply(resource, definition):
    definition['metadata']['annotations'][LAST_APPLIED_CONFIG_ANNOTATION] = definition
    try:
        current = resource.get(name=definition['metadata']['name'], namespace=definition['metadata']['namespace']).to_dict()
    except NotFoundError:
        return resource.create(body=definition)
    last_applied = current['metadata']['annotations'].get(LAST_APPLIED_CONFIG_ANNOTATION)
    if last_applied:
        last_applied = yaml.load(last_applied)
        del current['metadata']['annotations'][LAST_APPLIED_CONFIG_ANNOTATION]
    else:
        return resource.patch(body=definition, name=definition['metadata']['name'], namespace=definition['metadata']['namespace'])

    patch = merge(last_applied, definition, current)
    if patch:
        return resource.patch(body=patch, name=definition['metadata']['name'], namespace=definition['metadata']['namespace'])
    else:
        return "No update necessary"


# The patch is the difference from current to modified without deletions, plus deletions
# from original to modified. To find it, we compute deletions, which are the deletions from
# original to modified, and delta, which is the difference from current to modified without
# deletions, and then apply delta to deletions as a patch, which should be strictly additive.
def merge(original, modified, current):
    base = {}
    deletions = get_deletions(original, modified)
    delta = get_delta(current, modified)
    base.update(deletions)
    base.update(delta)
    return base


def get_deletions(original, modified):
    patch = {}
    for k, original_value in original.items():
        modified_value = modified.get(k)
        if modified_value is None:
            patch[k] = None
            continue
        if type(original_value) != type(modified_value):
            continue
        if isinstance(original_value, dict):
            p = get_deletions(original_value, modified_value)
            if p:
                patch[k] = p
        elif isinstance(original_value, (list, tuple)):
            # I have no idea what to do here
            pass
    return patch


def get_delta(current, modified):
    patch = {}
    for k, modified_value in modified.items():
        current_value = current.get(k)
        if current_value is None:
            patch[k] = modified_value
            continue
        if modified_value == current_value:
            continue
        if type(modified_value) != type(current_value):
            patch[k] = modified_value
        elif isinstance(modified_value, dict):
            p = get_delta(current_value, modified_value)
            if p:
                patch[k] = p
        elif isinstance(current_value, (list, tuple)):
            # I have no idea what to do here
            patch[k] = modified_value
        else:
            patch[k] = modified_value
    return patch
