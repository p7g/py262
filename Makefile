.PHONY: lint test format

lint:
	@./hooks/scripts/03-lint-python

format:
	@./hooks/scripts/01-order-imports
	@./hooks/scripts/02-format-python

test:
	@python -m unittest
