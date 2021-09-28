.PHONY: all \
		setup \
		db \
		test \
		black \
		flake8 \
		mypy \
		run

venv/bin/activate: ## alias for virtual environment
	python3 -m venv venv

setup: venv/bin/activate ## project setup
	. venv/bin/activate; pip install pip wheel setuptools
	. venv/bin/activate; pip install -r requirements.txt

db: venv/bin/activate ## run migrations
	. venv/bin/activate; python3 manage.py migrate

run: venv/bin/activate ## run
	. venv/bin/activate; python3 manage.py runserver

test: venv/bin/activate ## test
	. venv/bin/activate; python3 manage.py test

black:
	. venv/bin/activate; black ./

flake8:
	. venv/bin/activate; flake8 --config=./setup.cfg

mypy:
	. venv/bin/activate; mypy
