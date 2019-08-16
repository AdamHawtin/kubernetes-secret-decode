.PHONY: install, freeze-requirements, install-dependencies, check, flake, test, build
install:
	pip install -r requirements.txt
	pip install -e .

freeze-requirements:
	pipenv lock -r > requirements.txt

install-dependencies:
	pipenv install --dev

check:
	pipenv check

flake:
	pipenv run flake8

test: check flake
	pipenv run pytest

build: install-dependencies test
