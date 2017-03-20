def pytest_addoption(parser):
    parser.addoption("--openshift-version", action="store", default=None,
                     help="Version of OpenShift to test against for functional tests")


def pytest_report_header(config):
    return "OpenShift verison: {}".format(config.getoption('--openshift-version'))
