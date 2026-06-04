.PHONY: setup
setup:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

.PHONY: check
check:
	flake8 --exclude .venv && pytest -vv
