setup:

	pip install -r requirements.txt
	mypy exchange_rates_for_a_day.py
	flake8 --ignore=E501 exchange_rates_for_a_day.py
	mypy library.py
	flake8 --ignore=E501 library.py

run: setup
	python exchange_rates_for_a_day.py
