.PHONY: test

test: test-lint test-unit test-integration

test-lint:
	flake8 .

test-unit:
	pytest test/unit -v -r s

test-integration:
	pytest test/integration -v -r s
