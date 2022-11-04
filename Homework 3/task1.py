# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The
# [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер
# символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3)
# - "The 3 symbol in 'Python' is 't' ".

def get_num_suffix(num: int) -> str:
    if num % 10 not in {1, 2, 3} or num % 100 in {11, 12, 13}:
        return 'th'
    else:
        return ('st', 'nd', 'rd')[(num - 1) % 10]


max_attempts_allowed = 5
attempt_counter = 0

while attempt_counter <= max_attempts_allowed:
    word = input('Веедіть слово/набір символів, в якому будемо шукати символ:').strip(' ')

    try:
        assert len(word) > 0
        symb_num = int(input(f'Введіть порядковий номер символу, який треба витягти зі слова '
                             f'(ціле число від 1 до {len(word)}):'))

        print(f'The {symb_num}{get_num_suffix(symb_num)} symbol in the word \"{word}\" is ----> \"{word[symb_num - 1]}\" <----')
        break

    except AssertionError:
        print('Помилка вводу: введіть не порожнє слово/набір символів')
    except ValueError:
        print('Помилка типу даних: введіть число')
    except IndexError:
        print('Помилка у номері символу: номер символу, має бути не більшим за довжину слова/введеного набору символів')

    attempt_counter += 1
    print('-'* 40)
    print(f'{"Це Ваша остання спроба," if attempt_counter == max_attempts_allowed - 1 else "Спроба"} '
          f'{attempt_counter} з {max_attempts_allowed} дозволених')

else:
    print('Спроби закінчились. Запустіть код із самого початку')