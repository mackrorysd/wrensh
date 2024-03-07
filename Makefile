test:
	pytest --cov=src/wrensh --cov-report term-missing tests/

build:
	python -m build
