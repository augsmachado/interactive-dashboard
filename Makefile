### Create and start a virtual environment
create-venv:
	python3 -m venv .venv && \
	source .venv/bin/activate

start-venv:
	source .venv/bin/activate

### Installing the dependencies in your machine
install:
	pip install --upgrade pip
	pip install -r requirements.txt --upgrade

### Run tests
tests:
	pytest tests

### Init reflex projects
init:
	reflex init

### Run local
run-local:
	reflex run --loglevel debug