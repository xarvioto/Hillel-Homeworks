# завдання 2
# апі погоди (всі токени я для вас вже прописав)
# https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=47503e85fabbabc93cff28c52398ae97&units=metric
# де city_name - назва міста на аглійській мові (наприклад, odesa, kyiv, lviv)
# результатом буде приблизно такий результат

# {"coord":{"lon":30.7326,"lat":46.4775},"weather":[{"id":803,"main":"Clouds","description":"broken clouds",
# "icon":"04n"}],"base":"stations","main":{"temp":13.94,"feels_like":12.8,"temp_min":13.94,"temp_max":13.94,
# "pressure":1021,"humidity":54,"sea_level":1021,"grnd_level":1015},"visibility":10000,"wind":{"speed":4.58,
# "deg":314,"gust":8.16},"clouds":{"all":73},"dt":1664909335,"sys":{"country":"UA","sunrise":1664855942,
# "sunset":1664897549},"timezone":10800,"id":698740,"name":"Odesa","cod":200}

# погода змінюється, як і місто. яке ви введете
# роздрукувати тепрературу та швидкість вітру. з вказівкою міста, яке було вибране


# unit of measurements taken from API documentation https://openweathermap.org/current#data
# wind.speed Wind speed. Unit Default: meter/sec, Metric: meter/sec, Imperial: miles/hour.
# wind.deg Wind direction, degrees (meteorological)
# For temperature in Celsius use units=metric
# for wind directions used http://snowfence.umn.edu/Components/winddirectionanddegrees.htm reference table

import requests
from pprint import pprint


# here I don't try to break the function by feeding it some unexpected input. I assume the input from API is fine int
def num_wind_direction_to_str_repr(deg_met: int) -> str:
    directions_16 = ('N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW')
    deg_sector = int((deg_met + 11.25) // 22.5 % 16)
    return directions_16[deg_sector]


# here I don't try to break the function either. I assume the input from API is fine json aka dict
def weather_print_shorter(weather_dict: dict):
    if weather_dict['cod'] == 200:  # if you input slightly wrong city name -
        # API returns small json like {"cod": 404, "message": "city not found"} (I managed to get 404 and 400 codes)
        # so who knows what other codes are possible. 200 - is OK for sure.

        shorter_weather_dict = {}

        city_name = weather_dict['name']
        shorter_weather_dict.update({'city_name': city_name})

        wind_direction_int = weather_dict['wind']['deg']
        # shorter_weather_dict.update({'wind deg': wind_direction_int})

        wind_speed = weather_dict['wind']['speed']
        shorter_weather_dict.update({'wind_speed': wind_speed})

        temperature = weather_dict['main']['temp']
        shorter_weather_dict.update({'temperature': temperature})

        print(f'In {city_name} the weather is the following:\n'
              f'Wind is {num_wind_direction_to_str_repr(wind_direction_int)} ({wind_direction_int} '
              f'meteorological degrees) at {wind_speed} meter/sec\n'
              f'The temperature is around {round(temperature)} degrees Celsius\n'
              f'OR the same in a dict:')
        print(shorter_weather_dict)
    else:
        print(f'Something went wrong. API returned response: {weather_dict["cod"]} - '
              f'{weather_dict["message"]}')


city_name_input = input('Please input city name, if you want to know the weather there (English only):\n')
# API ignores cases, strips spaces from both sides by itself, so we don't need to deal with them on our side at least


weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name_input}' \
              f'&appid=47503e85fabbabc93cff28c52398ae97&units=metric'

# ConnectionError is frequent one for me these days.
try:
    weather_get_response = requests.get(weather_url)
except ConnectionError as ec:
    print(f'ERROR: Connection error. Please you have access to the internet')
    pprint(ec, width=150)
except Exception as e:
    print(f'ERROR: Something definitely got wrong while getting response from'
          f' {weather_url}')
    pprint(e, width=150)

else:
    weather_response_dict = weather_get_response.json()
    weather_print_shorter(weather_response_dict)
