# Створіть клас, який реалізує підключення до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ).
# Обʼєкт класу повинен вміти отримувати курс валют станом на певну дату. Обʼєкт класу повинен вміти записати курси
# в текстовий файл. Назва файлу повинна містити дату на яку шукаємо курс, наприклад:
#  21_11_2019.txt
# Дані в файл запишіть у вигляді списку :
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
# P.S. Архітектура класу - на розсуд розробника. Не забувайте про DRY, KISS, YAGNI, SRP та перевірки!)


from library import WriterExchangeRatesNbuIntoFile
import datetime


if __name__ == "__main__":

    # For now all actual and effective API parameters are set as default values durin WriterExchangeRatesNBU init
    first_instance_nbu_api_handler = WriterExchangeRatesNbuIntoFile()

    # Still, if something changes insignificantly - it is easy to adapt by passing some changed parameters as kwargs
    # without changing the code for some brief period of time
    api_kwargs = {'url_nbu_api_without_keys': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange',
                  'date_key_format': "%Y%m%d", 'currency_short_name_key': 'cc',
                  'currency_rate_key': 'rate', "exchange_date_key": 'exchangedate'}

    second_instance_nbu_api_handler = WriterExchangeRatesNbuIntoFile(**api_kwargs)

    print('Request 1 and 2: There might be dates with absent data (deep past or future). '
          'API gives completely valid but empty responses)')
    first_instance_nbu_api_handler.write_rates_as_of_date_into_file('19691215')
    first_instance_nbu_api_handler.write_rates_as_of_date_into_file('20231215')

    print('Request 3. Faulty date means showing error message, aborting the attempt')
    first_instance_nbu_api_handler.write_rates_as_of_date_into_file('20212114')

    print('Request 4 and 5. finally the valid date, should return good content resulting into a file creation')
    first_instance_nbu_api_handler.write_rates_as_of_date_into_file('20211215')
    second_instance_nbu_api_handler.write_rates_as_of_date_into_file('20220807')

    print('Request 6. Empty date parameter during a call of write_rates method - means to get rates requested '
          'as current date, as for now')
    second_instance_nbu_api_handler.write_rates_as_of_date_into_file()

    print('Request 7. It works as well if you feed a datetime object to it. '
          'Datetime has 3 minimum requirement parameters: year, month and day, which is very convenient')
    some_date = datetime.datetime(year=2012, month=10, day=20)
    second_instance_nbu_api_handler.write_rates_as_of_date_into_file(some_date)
