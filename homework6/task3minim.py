# 3. Перепишіть за допомогою функцій вашу программу "Касир в кінотеатрі", яка буде виконувати наступне:
# Попросіть користувача ввести свсвій вік.
# - якщо користувачу менше 7 - вивести "Тобі ж <> <>! Де твої батьки?"
# - якщо користувачу менше 16 - вивести "Тобі лише <> <>, а це е фільм для дорослих!"
# - якщо користувачу більше 65 - вивести "Вам <> <>? Покажіть пенсійне посвідчення!"
# - якщо вік користувача містить 7 - вивести "Вам <> <>, вам пощастить"
# - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <> <>, білетів всеодно нема!"
# Замість <> <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік. Для будь-якої
# відповіді форма слова "рік" має відповідати значенню віку користувача (1 - рік, 22 - роки, 35 - років і тд...).
# Наприклад :
# "Тобі ж 5 років! Де твої батьки?"
# "Вам 81 рік? Покажіть пенсійне посвідчення!"
# "Незважаючи на те, що вам 42 роки, білетів всеодно нема!"
# solution - use cashier_at_cinema_algo function, 3 optional key arguments:
# cashier_greeting='Напишіть, скільки Вам років (на приклад 30 чи 2.5):,
# min_age_allowed=1, max_age_allowed=100,


def year_word_ending_ua(years_num: int) -> str: # I assume people tries inputting only ints, as predicted. Floats will do either
    years_num = abs(years_num)
    if years_num % 10 == 1 and years_num % 100 != 11:
        return 'рік'
    elif years_num % 10 in {2, 3, 4} and years_num % 100 not in {12, 13, 14}:
        return 'роки'
    else:
        return 'років'


def cashier_at_cinema_algo(
                        cashier_greeting=f'Напишіть, скільки Вам років (ціле число, на приклад 30):',
                        min_age_allowed: int = 1,
                        max_age_allowed: int = 100,
                        user_input_num=0
                        ):
    while True:
        try:

            visitor_age = int(input(cashier_greeting).strip(' '))

            assert min_age_allowed <= visitor_age <= max_age_allowed

        except ValueError as e:
            print(f'Error: Should be a whole number (like 30)')
            print('-' * 40)
        except AssertionError as e:
            print(f'Error: Should be a number between {min_age_allowed} and {max_age_allowed}')
            print('-' * 40)
        else:
            age_with_ending = f'{visitor_age} {year_word_ending_ua(visitor_age)}'
            if '7' in str(visitor_age):
                print(f'Вам {age_with_ending}, Вам пощастить!')
            elif visitor_age < 7:
                print(f'Тобі ж {age_with_ending}! Де твої батьки?')
            elif visitor_age < 16:
                print(f'Тобі лише {age_with_ending}, а це е фільм для дорослих!')
            elif visitor_age > 65:
                print(f'Вам {age_with_ending}? Покажіть пенсійне посвідчення!')
            else:
                print(f'Незважаючи на те, що вам {age_with_ending}, білетів всеодно нема!')


cashier_at_cinema_algo()
