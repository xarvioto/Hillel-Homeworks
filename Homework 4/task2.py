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

result_dict = {}

# is it YAGNI? Here i store both target keys and corresponding values. Because it seems likely for me,
# that the next step will be something concerned to both stores AND prices
for key, value in price_dict.items():
    if lower_limit <= value <= upper_limit:
        result_dict.update({key: value})

# The fiddling to make representation fits the example output representation. I mean double quotes and comma ceparation.
# It does not do 'work', but it is an interesting exercise anyways.
# There might be an easier way, but I did not manage to come up with one
result_list = ['\"' + key + '\"' for key in result_dict.keys()]

print(f'Here is the list of keys having values <={lower_limit} AND >={upper_limit}:\n' +
      '----->   ' + ', '.join(result_list) if len(result_list) > 0 else 'None')





