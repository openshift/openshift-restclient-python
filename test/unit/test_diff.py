from openshift.dynamic.apply import recursive_diff

tests = [
    dict(
        before = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        after = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        expected = None
    ),
    dict(
        before = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        after = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8081, name="http")])
        ),
        expected = (
            dict(spec=dict(ports=[dict(port=8080, name="http")])),
            dict(spec=dict(ports=[dict(port=8081, name="http")]))
        )
    ),
    dict(
        before = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http"), dict(port=8081, name="https")])
        ),
        after = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8081, name="https"), dict(port=8080, name="http")])
        ),
        expected = None
    ),

    dict(
        before = dict(
            kind="Pod",
            metadata=dict(name="foo"),
            spec=dict(containers=[dict(name="busybox", image="busybox",
                                       env=[dict(name="hello", value="world"),
                                            dict(name="another", value="next")])])
        ),
        after = dict(
            kind="Pod",
            metadata=dict(name="foo"),
            spec=dict(containers=[dict(name="busybox", image="busybox",
                                       env=[dict(name="hello", value="everyone")])])
        ),
        expected=(dict(spec=dict(containers=[dict(name="busybox", env=[dict(name="another", value="next"), dict(name="hello", value="world")])])),
                  dict(spec=dict(containers=[dict(name="busybox", env=[dict(name="hello", value="everyone")])])))
    ),
    ]


def test_diff():
    for test in tests:
        assert(recursive_diff(test['before'], test['after']) == test['expected'])
