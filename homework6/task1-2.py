# 1. Напишіть функцію, що приймає один аргумент будь-якого типу та повертає цей аргумент, перетворений на float. Якщо
# перетворити не вдається функція має повернути 0.
# solution - use convert_to_float function, one arg of Any type


# 2. Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів (int, float) - повернути перемножене значення цих аргументів,
# якщо обидва аргументи це строки (str) - обʼєднати в одну строку та повернути
# у будь-якому іншому випадку повернути кортеж з цих аргументів
# solution - use two_args_madness function, two arg of Any type


# quite a few unexpected strings could be converted to float acc to documentation, so there is no other way,
# except trying to convert and watch what happens when it tries convert to float
def convert_to_float(object_to_check):
    try:
        return float(object_to_check)
    except Exception as e:
        return 0


assert convert_to_float(2) == 2.0
assert convert_to_float(2.0) == 2.0
assert convert_to_float('2') == 2.0
assert convert_to_float('2.') == 2.0
assert convert_to_float('2.0') == 2.0
assert convert_to_float('2.0.') == 0
assert convert_to_float('qwe') == 0
assert convert_to_float([1, 2, 3.0]) == 0
assert convert_to_float(' ') == 0
assert convert_to_float(None) == 0


# Unfortunately, isinstance(True, (int, float)) returns True, because of num  hidden nature of bools
# -> 'type(arg) in (int, float)' is used instead, even if 'isinstance' is fancier
def two_args_madness(arg_1, arg_2):
    if type(arg_1) in (int, float) and type(arg_2) in (int, float):
        return arg_1 * arg_2
    elif isinstance(arg_1, str) and isinstance(arg_2, str):
        return arg_1 + arg_2
    else:
        return arg_1, arg_2


assert two_args_madness(2, 2.0) == 4.0
assert two_args_madness('2', '2.0') == '22.0'
assert two_args_madness('2', 2.0) == ('2', 2.0)
assert two_args_madness(True, 2.0) == (True, 2.0)
assert two_args_madness(None, True) == (None, True)
