# 1. в файлі library написати функцію, котра приймає два числа та показник степеня - теж число. назва функції та
# аннотація мають бути такими, щоб докстрінга взагалі не була потрібна (что бажає - читаємо Чистий код)
# 2. функція перемножує два числа, їх добуток підносить до степеня та повертає значення
# 3. два числа, які перемножаються, можуть бути тільки позиційними аргументами
# 4. показник степеня може бути тільки іменованим аргументом
# 5. закешувати результат роботи функції (декоратор cache). подивитися, як вплинув декоратор на роботу mypy та
# на обмеження на іменованих та порядкових аргументів
# 6. імпортувати написану функцію в файл main, і там її позапускати з виведенням логів у консоль (print)
# 7. flake8 mypy pytest та запис всіх залежностей в файл requirements.txt - всі встановлення та послідуючий запис
# в файл мають виконуватися однією командою make setup
# 8. написати тести для цієї функції. тести мають в тому числі включати перевірку на помилки типу TypeError
# anv ValueError... додатково зверніть увагу, що має бути наступний тест: при аргументах -2 (мінус два), 3,
# та показнику степеня 2, результат має бути 36 (позитивне значення при парному степеню). перевірте також типи
# отримуваних значень
# 9. організуйте запуск ВСЬОГО коду однією командою make run. я, як викладач, просто завантажу вашу роботу
# (3 файла пітона, залежності та мейкфайл) в робочий проект (з існуючим у мене віртуальним оточенням),
# запущу дану команду і отримаю результат роботи в терміналі. без цього перевірка безпосередньо коду навіть
# не буде проводитися - відразу на перездачу (як в автошколі - завалив теорію, за руль не пускають)
# 10. зауважу, що в мейкфайлі у вас має бути лише дві команди на запуск. DRY

from library import make_positive_power_of_two_real_nums_product

print('3 by 2.5 power 3: -->', make_positive_power_of_two_real_nums_product(3, 2.5, power_num=3))

print('-3 by 5 power 2: -->', make_positive_power_of_two_real_nums_product(-3, 5, power_num=2))

print('1 by 5 power 5: -->', make_positive_power_of_two_real_nums_product(1, 5, power_num=5))
