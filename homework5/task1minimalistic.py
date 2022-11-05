# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті
# (дані не фейкові, оновлюються в режимі реального часу)

from pprint import pprint
import requests

astros_url = 'http://api.open-notify.org/astros.json'

try:
    astros_get_response = requests.get(astros_url)
except Exception as e:
    pprint(e, width=150)

else:
    astros_get_dict = astros_get_response.json()
    astros_in_space_dict = astros_get_dict['people']

    astros_in_space_names_list = []

    for astronaut in astros_in_space_dict:
        astros_in_space_names_list.append(astronaut['name'])

    if astros_in_space_names_list:
        print(f'List of astronauts in space:')
        print(astros_in_space_names_list)
    else:
        print(f'We are missing info that somebody is in space at the moment. There might be nobody')