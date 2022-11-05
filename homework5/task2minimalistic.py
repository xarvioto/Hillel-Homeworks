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

import requests
from pprint import pprint

city_name_input = 'kyiv'

weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name_input}' \
              f'&appid=47503e85fabbabc93cff28c52398ae97&units=metric'

try:
    weather_get_response = requests.get(weather_url)
except Exception as e:
    pprint(e, width=150)

else:
    weather_in_city_dict = weather_get_response.json()

    if weather_in_city_dict['cod'] == 200:
        shorter_weather_dict = {}
        shorter_weather_dict.update({'city_name': weather_in_city_dict['name']})
        shorter_weather_dict.update({'wind_speed': weather_in_city_dict['wind']['speed']})
        shorter_weather_dict.update({'temperature': weather_in_city_dict['main']['temp']})

        print(f'Weather in {shorter_weather_dict["city_name"]} in dict:')
        print(f'---> {shorter_weather_dict}')
    else:
        print(f'Something went wrong. API returned response: {weather_in_city_dict["cod"]} - '
              f'{weather_in_city_dict["message"]}')
