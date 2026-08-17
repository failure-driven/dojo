default: check

.PHONY: lint
lint:
	uv run flake8 --exclude .venv

.PHONY: test
test:
	uv run pytest -vvv

.PHONY: check
check: lint test

.PHONY: demo
demo:
	@uv run rover '{"x":0,"y":0,"direction":"N","commands":["l","l","r"]}'
