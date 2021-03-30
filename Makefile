.PHONY: test

ARTIFACT_DIR ?= ./

test: test-lint test-unit test-integration

test-lint:
	flake8 . && (flake8 --format junit-xml . > ${ARTIFACT_DIR}/test-lint.junit.xml)

test-unit:
	pytest test/unit -v -r s --junitxml=${ARTIFACT_DIR}/test-unit.junit.xml

test-integration:
	pytest test/integration -v -r s --junitxml=${ARTIFACT_DIR}/test-integration.junit.xml
