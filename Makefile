clean:
	git clean -dfX

test:
	pytest --cov=src/wrensh --cov-report term-missing tests/

package:
	python -m build

publish:
	twine upload dist/*
