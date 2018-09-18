from pytest_bdd import scenario, then, when, parsers


@scenario('create.feature', 'Create a resource again')
def test_create_a_resource_again():
    """Create a resource again."""
    pass


@scenario('create.feature', 'Create a resource for the first time')
def test_create_a_resource_for_the_first_time():
    """Create a resource for the first time."""
    pass


@then(parsers.parse('<group_version>.<kind> <name> exists in <namespace>'))
def resource_in_namespace(admin_client, group_version, kind, name, namespace):
    """<group_version>.<kind> <name> exists in <namespace>."""
    resource = admin_client.resources.get(api_version=group_version, kind=kind)
    instance = resource.get(name, namespace)
    assert instance.metadata.name == name
    assert instance.metadata.namespace == namespace


@when(parsers.parse('I create <group_version>.<kind> <name> in <namespace>'))
def create_resource_in_namespace(context, client, group_version, kind, name, namespace, definition_loader):
    """I create <group_version>_<kind>_<namespace>_<name>.yaml."""
    resource = client.resources.get(api_version=group_version, kind=kind)
    context["instance"] = resource.create(body=definition_loader(name), namespace=namespace)


@when(parsers.parse('I try to create <group_version>.<kind> <name> in <namespace>'))
def attempt_create_resource_in_namespace(context, client, group_version, kind, name, namespace, definition_loader):
    """I <action> <group_version>_<kind>_<namespace>_<name>.yaml."""
    resource = client.resources.get(api_version=group_version, kind=kind)
    try:
        context["instance"] = resource.create(body=definition_loader(name), namespace=namespace)
    except Exception as e:
        context['exc'] = e
