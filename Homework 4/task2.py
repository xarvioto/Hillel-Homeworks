# Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами: {
# "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166,
# "the_partner": 38.988, "store": 37.720, "rozetka": 38.003}. Напишіть код, який знайде і виведе на екран назви
# магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною. Наприклад:

# lower_limit = 35.9
# upper_limit = 37.339
# > match: "x-store", "main-service"

lower_limit = 35.32
upper_limit = 38.12
price_dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "rozetka": 38.003
}

result_list = []

for store, price in price_dict.items():
    if lower_limit <= price <= upper_limit:
        result_list.append(store)

# The fiddling to make representation fits the representation of the example output. I mean stores wrapped in "" .
print(f'Here is the list of stores having prices <={lower_limit} AND >={upper_limit}:\n' +
      '----->   ' + ', '.join([f'\"{word}\"' for word in result_list]) if len(result_list) > 0 else 'None')





