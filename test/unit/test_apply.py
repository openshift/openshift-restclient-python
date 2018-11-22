# Test ConfigMapHash and SecretHash equivalents
# tests based on https://github.com/kubernetes/kubernetes/pull/49961

from openshift.dynamic.apply import merge

tests = [
    dict(
        last_applied = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", two="2")
        ),
        desired = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", two="2")
        ),
        expected = {}
    ),
    dict(
        last_applied = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", two="2")
        ),
        desired = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", two="2", three="3")
        ),
        expected = dict(data=dict(three="3"))
    ),
    dict(
        last_applied = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", two="2")
        ),
        desired = dict(
            kind="ConfigMap",
            metadata=dict(name="foo"),
            data=dict(one="1", three="3")
        ),
        expected = dict(data=dict(two=None, three="3"))
    ),
    dict(
        last_applied = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        desired = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        expected = {}
    ),
    dict(
        last_applied = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8080, name="http")])
        ),
        desired = dict(
            kind="Service",
            metadata=dict(name="foo"),
            spec=dict(ports=[dict(port=8081, name="http")])
        ),
        expected = dict(spec=dict(ports=[dict(port=8081, name="http")]))
    ),
]


def test_merges():
    for test in tests:
        assert(merge(test['last_applied'], test['desired'], test.get('actual', test['last_applied'])) == test['expected'])
