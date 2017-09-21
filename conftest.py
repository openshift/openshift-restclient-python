def pytest_addoption(parser):
    parser.addoption("--openshift-version", action="store", default=None,
                     help="Version of OpenShift to test against for functional tests")


def pytest_report_header(config):
    return "OpenShift version: {}".format(config.getoption('--openshift-version'))
