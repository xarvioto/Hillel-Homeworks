setup:

	pip install -r requirements.txt
	mypy triangle.py
	flake8 --ignore=E501 triangle.py
	mypy test_triangle.py
	flake8 --ignore=E501,F841 test_triangle.py
	pytest

run: setup
	python triangle.py
