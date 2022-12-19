setup:

	pip install -r requirements.txt
	mypy game.py
	flake8 --ignore=E501,F841 game.py
	mypy library.py
	flake8 --ignore=E501 library.py
	mypy test_library.py
	flake8 --ignore=E501,F841 test_library.py
	pytest

run: setup
	python game.py
