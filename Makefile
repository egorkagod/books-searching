PYTHON = ${shell which python3}

.PHONY: test docker-test run build

test:
	@$(PYTHON) -m pytest -s app/tests

docker-test:
	@$(PYTHON) -m pytest -s app/tests/integration

run:
	docker-compose up

build:
	docker-compose up --build