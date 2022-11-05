# завдання 1
# урл http://api.open-notify.org/astros.json
# вивести список всіх астронавтів, що перебувають в даний момент на орбіті
# (дані не фейкові, оновлюються в режимі реального часу)

from pprint import pprint
import requests

astros_url = 'http://api.open-notify.org/astros.json'

# ConnectionError is frequent one for me these days.
try:
    astros_get_response = requests.get(astros_url)

except ConnectionError as ec:
    print(f'ERROR: Connection error. Please you have access to the internet')
    pprint(ec, width=150)
except Exception as e:
    print(f'ERROR: Something definitely got wrong while getting response from'
          f' {astros_url}')
    pprint(e, width=150)

# is it OK to put all your code in else of try-except contraption? else may grow way too big
else:
    astros_get_dict = astros_get_response.json() # Here I assume the input from API is fine json aka dict
    if astros_get_dict['message'] == 'success':
        astros_in_space_dict = astros_get_dict['people']

        astros_in_space_names_list = []

        for astronaut in astros_in_space_dict:
            astros_in_space_names_list.append(astronaut['name'])

        if astros_in_space_names_list:
            print(f'There are {len(astros_in_space_names_list)} of astronauts in space at the moment. The list is below:')
            # We don't know how many astronauts there will be in the future.
            # If many - compact representation is just essential
            # bad side of pprint, is that it wraps long strings with '' and very long with () to make it clear
            # that it is str, where is starts and where ends.
            pprint(", ".join(astros_in_space_names_list), width=150)
        else:
            print(f'There might be nobody in space right now')
    else:
        print(f'Something went wrong. API returned response: {astros_get_dict["message"]}')  # I don't know if there
        # other responses except 'success', but if there are - here is else statement for the case
        # There is nothing about it in brief documentation http://open-notify.org/Open-Notify-API/People-In-Space/

