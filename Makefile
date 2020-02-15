SHELL := /bin/bash
.PHONY: all clean install test 

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: clean install test 

test:
	poetry run pytest tests -v

magic:
	$(SHELL) egg.sh

generate-env:
	cp .env.example .env

prepare-db:
	poetry run flask drop-db
	poetry run flask create-db
	poetry run flask populate-db

install:
	$(MAKE) generate-env
	pip install --upgrade pip
	pip install poetry
	poetry install
	$(MAKE) prepare-db

run:
	poetry run flask run

deploy:
	docker-compose build
	docker-compose up -d
	$(MAKE) magic

down:
	docker-compose down

clean:
	@find . -name '*.pyc' -exec rm -rf {} \;
	@find . -name '__pycache__' -exec rm -rf {} \;
	@find . -name 'Thumbs.db' -exec rm -rf {} \;
	@find . -name '*~' -exec rm -rf {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build