.PHONY: lint test

lint:
	@pylint py262
	@mypy py262

test:
	@python -m unittest
