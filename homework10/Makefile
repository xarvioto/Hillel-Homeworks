setup:

	pip install -r requirements.txt
	mypy main.py
	flake8 --ignore=E501 main.py
	mypy library.py
	flake8 --ignore=E501 library.py
	mypy test_library.py
	flake8 --ignore=E501,E226 test_library.py
	pytest

run: setup

	python main.py
