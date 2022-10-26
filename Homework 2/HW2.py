# Напишіть программу "Касир в кінотеватрі", яка буде виконувати наступне:
#
# Попросіть користувача ввести свсвій вік (можно використати константу або input()).
# - якщо користувачу менше 7 - вивести повідомлення "Де твої батьки?"
# - якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
# - якщо користувачу більше 65 - вивести повідомлення "Покажіть пенсійне посвідчення!"
# - якщо вік користувача з двох однакових цифр - вивести повідомлення "Як цікаво!"
# - у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"
#
# P.S. На екран має бути виведено лише одне повідомлення, якщо вік користувача з двох однакових цифр то має бути
# виведено тільки відповідне повідомлення! Також подумайте над варіантами, коли введені невірні або неадекватні дані.

# There is an attempt to filter out all invalid values of age. In an arbitrary manner
arb_age_up_limit = 150
arb_age_low_limit = 2

input_is_valid = False

while not input_is_valid:

    try:
        cust_age = int(float(input('Напишіть, скільки Вам років (на приклад 30 чи 2.5):').replace(' ', '').replace(',', '.')))
        assert arb_age_low_limit <= cust_age < arb_age_up_limit
        input_is_valid = True
    except ValueError:
        print('Помилка: Будь ласка, введіть Ваш вік як число')
    except AssertionError:
        print('Помилка: Будь ласка, введіть Ваш справжній вік')


if cust_age < 7:
    print('Де твої батьки?')
elif str(cust_age) == str(cust_age)[-1::-1] and len(str(cust_age)) == 2:
    print('Як цікаво!')
elif cust_age < 16:
    print('Це фільм для дорослих!')
elif 65 <= cust_age: # There is <= instead of < completely on purpose. It seems like it makes more sense.
    print('Покажіть пенсійне посвідчення!')
else:
    print("А білетів вже немає!")
