import requests
import datetime


class RequestNBURates:
    """
    Handles requestes to NBU currency exchange rates API
    Accepts as parameters an URL and requested date
    Expects to get json in response content
        Response is accessible via json api_response attribute
        json content is accessible via json_content attribute

    Raises errors if:
        response code != 200
        content type != json/application
        content fails to be interpreted as json by requests.json method
    """
    url_nbu_api: str
    api_response: requests.models.Response
    json_content: list

    def __init__(self, url_nbu_api: str, requested_date: str):
        self.url_nbu_api = url_nbu_api
        self.request_rates_via_api(requested_date)

    def request_rates_via_api(self, date_requested: str):

        def make_request_to_api():
            try:
                return requests.get(self.url_nbu_api, timeout=5)
            except ConnectionError as ce:
                raise ConnectionError(ce)
            except Exception as e:
                raise Exception(e)

        def check_200_response_code_else_error(response_to_request: requests.models.Response):
            """Considers 200 code as the only successful code that returns the content we need"""
            if response_to_request.status_code != 200:
                raise ValueError(f'request returned not 200 status code. Actual status code : '
                                 f'{response_to_request.status_code} \n'
                                 f'Header of response:\n {response_to_request.headers}.\n'
                                 f'Processing of the request goes no further.')

        def check_json_content_type_else_error(response_to_request: requests.models.Response):
            if 'application/json' not in response_to_request.headers.get('Content-Type', ''):
                raise TypeError(f'Error: Response contains not \'application/json\' or no Content-Type: '
                                f'{response_to_request.headers.get("Content-Type", "")}'
                                f'Processing of the request goes no further.')

        def response_to_json_else_error(response_to_request: requests.models.Response):
            try:
                return response_to_request.json()
            except Exception as e:
                raise Exception(f'Error: failed to convert response content into json. Please check the content out:\n '
                      f'{str(response_to_request.content)}\n {e}')

        self.api_response = make_request_to_api()
        check_200_response_code_else_error(self.api_response)
        check_json_content_type_else_error(self.api_response)
        response_converted_to_json = response_to_json_else_error(self.api_response)

        self.json_content = response_converted_to_json


class WriterExchangeRatesNbuIntoFile:
    """
    Calls request to NBU API, checks that json response has expected keys for valid interpratation.
    Writes content of successful and non-empty json responds into file named dd_mm_yyyy.txt

    In order to allow multiple requests in a row (valid and not valid, successful and not successful):
        In case of any error - catches errors, provides error messages in terminal while preventing of program crash.
    """

    _date_in_work: datetime.date
    api_valid_response: RequestNBURates
    currency_short_name_key: str
    currency_rate_key: str
    url_nbu_api_without_keys: str
    date_key_format: str

    def __init__(self, url_nbu_api_without_keys='https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange',
                 date_key_format="%Y%m%d", currency_short_name_key='cc', currency_rate_key='rate',
                 exchange_date_key='exchangedate'):

        self.url_nbu_api_without_keys = url_nbu_api_without_keys
        self.date_key_format = date_key_format
        self.currency_short_name_key = currency_short_name_key
        self.currency_rate_key = currency_rate_key
        self.exchange_date_key = exchange_date_key
        self.api_valid_response = None
        self._date_in_work = None

    @property
    def date_in_work(self):
        return self._date_in_work

    @date_in_work.setter
    def date_in_work(self, date_value: str | datetime.date):
        """
        Set _date_in_work as dateime objects.
        Tries to convert from string into a datetime object if string passed to a setter
        Args:
            date_value (str | datetime.date):
        """

        if isinstance(date_value, datetime.date):
            self._date_in_work = date_value
        else:
            try:
                self._date_in_work = datetime.datetime.strptime(date_value, self.date_key_format).date()
            except ValueError:
                raise ValueError(f'Error: \'{date_value}\' could have not be decoded as a real date. Attempt aborted. '
                                 f'Please provide valid date in \'{self.date_key_format}\' format as a string, '
                                 f'aka \'{datetime.datetime.now().strftime("%Y%m%d")}\'')

    @property
    def date_in_work_as_str_key(self):
        return self.date_in_work.strftime(self.date_key_format)

    @property
    def url_nbu_api(self):
        return f'{self.url_nbu_api_without_keys}?date={self.date_in_work_as_str_key}&json'

    def write_rates_as_of_date_into_file(self, date_to_write_rates_into_file: str | datetime.date = ''):

        currency_abbr_key = self.currency_short_name_key
        rate_key = self.currency_rate_key
        api_date_key = self.exchange_date_key

        def entry_has_all_necessary_keys(dict_to_check):
            return dict_to_check.get(currency_abbr_key, '') and dict_to_check.get(rate_key, '')

        def date_in_entry_matches_working_date(dict_to_check):
            return dict_to_check.get(api_date_key, '') == self.date_in_work.strftime("%d.%m.%Y")

        def create_file_and_write_content_stylized():

            with open(f'{self.date_in_work.strftime("%d_%m_%Y")}.txt', 'w') as exchange_rates_file:
                json_length = len(self.api_valid_response.json_content)

                if self.api_valid_response.json_content:

                    for num, one_currency_dict in enumerate(self.api_valid_response.json_content, start=1):
                        if entry_has_all_necessary_keys(one_currency_dict) and \
                                date_in_entry_matches_working_date(one_currency_dict):
                            next_string = "\n" if num < json_length else ""
                            exchange_rates_file.write(f'{num}. {one_currency_dict[currency_abbr_key]} '
                                                      f'to UAH: {one_currency_dict[rate_key]} {next_string}')
                        else:
                            exchange_rates_file.write(f'{num}. Could not find expected keys in json entry: '
                                                      f'{str(one_currency_dict)}')

                    print(f'{exchange_rates_file.name} file was successfully created')

                else:
                    print(f'Request with date {self.date_in_work_as_str_key} returned valid but empty json response. '
                          f'There might be no rates data on {self.date_in_work.strftime("%d.%m.%Y")}. '
                          f'File was not created')

        try:
            if not date_to_write_rates_into_file:
                self.date_in_work = datetime.datetime.now().date()
            else:
                self.date_in_work = date_to_write_rates_into_file
        except Exception as e:
            print(e)
        else:
            try:
                self.api_valid_response = RequestNBURates(self.url_nbu_api, self.date_in_work_as_str_key)
            except Exception as e:
                print(e)
            else:
                create_file_and_write_content_stylized()
