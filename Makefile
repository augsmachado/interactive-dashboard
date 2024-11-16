### Create and start a virtual environment
create-venv:
	python3 -m venv .venv

start-venv:
	source .venv/bin/activate

### Installing the dependencies in your machine
install:
	pip install --upgrade pip
	pip install -r airflow/requirements.txt --upgrade

### Run tests
tests:
	pytest tests