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
# solution - use cashier_at_cinema_algo function, 5 optional key arguments:
# cashier_greeting, min_age_allowed=1, max_age_allowed=100,
# max_attempts_allowed=0 for decorator (which do infinite or finite loops)
# user_input_bypass=0 - make bypass for all the manual number input and validation. Takes parameter value
# instead of user manual input

def get_number_from_input(prompt_str: str):
    try:
        return int(float(input(prompt_str).replace(' ', '').replace(',', '.')))
    except ValueError as e:
        raise e  # Error is treated somewhere, at higher level


def validate_int_between(number: int, first_number: int, second_number: int) -> bool:
    return min(first_number, second_number) <= number <= max(first_number, second_number)


def year_word_ending_ua(
        years_num: int) -> str:  # i assume people tries inputting only ints, as predicted. Floats will do either
    years_num = abs(years_num)
    if years_num % 10 == 1 and years_num % 100 != 11:
        return 'рік'
    elif years_num % 10 in {2, 3, 4} and years_num % 100 not in {12, 13, 14}:
        return 'роки'
    else:
        return 'років'


def print_cashier_response(visitor_age: int):
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

# Decor function gets an argument 'max_attempts_allowed' from wrapped function (if there is none - uses 0 by default)
# wrap it with either finite or infinite cycle of trial. 0 for indefinite
def decor_cycle_max_or_infinite_attempts(func):
    def wrapper_with_kwargs(max_attempts_allowed: int = 0, **kwargs):
        if max_attempts_allowed <= 0:  # Please, don't put negative numbers here. It would not make a lot of sense
            # but negatives are 0 for this purpose
            while True:
                try:
                    func(**kwargs)
                    break
                except Exception as e:
                    print('-' * 40)
        else:
            for attempt_num in range(1, max_attempts_allowed + 1):
                try:
                    func(**kwargs)
                    break
                except Exception as e:
                    print('-' * 40)
                    if attempt_num == max_attempts_allowed:
                        print(f'Спроби закінчились. Запустіть код знову')
                    else:
                        last_or_not_attempt_str = 'Остання спроба: ' if max_attempts_allowed - attempt_num == 1 else 'Наступна спроба: '
                        print(f'{last_or_not_attempt_str} {attempt_num + 1} з {max_attempts_allowed} дозволених')

    return wrapper_with_kwargs


@decor_cycle_max_or_infinite_attempts
def cashier_at_cinema_algo(
        cashier_greeting=f'Напишіть, скільки Вам років (на приклад 30 чи 2.5):',
        min_age_allowed: int = 1,
        max_age_allowed: int = 100,
        user_input_bypass: int = 0
):
    if user_input_bypass:
        return print_cashier_response(user_input_bypass)
    else:
        try:
            buyer_age = get_number_from_input(prompt_str=cashier_greeting)

            assert validate_int_between(
                number=buyer_age,
                first_number=min_age_allowed,
                second_number=max_age_allowed
            )
        except ValueError as e:
            print(f'Error: Should be a number (like 30 or 2.5)')
            raise e  # Error is treated somewhere, at higher level
        except AssertionError as e:
            print(f'Error: Should be a number between {min_age_allowed} and {max_age_allowed}')
            raise e  # Error is treated somewhere, at higher level
        else:
            return print_cashier_response(buyer_age)


cashier_at_cinema_algo(max_attempts_allowed=3)  # max_attempts_allowed=0 for indefinite input attempts
