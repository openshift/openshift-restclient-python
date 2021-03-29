.PHONY: test

test: test-lint test-unit test-integration
	@echo "This will run all tests"

test-lint:
	@echo "This will run linting jobs"

test-unit:
	@echo "This will run unit tests"

test-integration:
	@echo "This will run integration tests"
