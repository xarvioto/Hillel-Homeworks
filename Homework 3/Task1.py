# 1. Напишіть код, який зформує строку, яка містить певну інформацію про символ за його номером у слові. Наприклад "The
# [номер символу] symbol in '[тут слово]' is '[символ з відповідним порядковим номером в слові]'". Слово та номер
# символу отримайте за допомогою input() або скористайтеся константою. Наприклад (слово - "Python" а номер символу 3)
# - "The 3 symbol in 'Python' is 't' ".


max_attempts_allowed = 5

# It may be seen as unlogical here to use 'for' instead of 'while', as well as there are too many ways out of loop,
# one more than necessary
# Ideally my 'for' shall never reach the end of its last iteration ('max_attempts_allowed +
# 1' - 1) But i used 'for' on purpose. ReasoningL 'while' is way less efficient in Python (consumes a way more
# resources and time while doing the same job) at least i've read such a thing: as 'for' logic in Python is written
# directly using C, but 'while' in Python is written using Python
for attempt_count in range(1, max_attempts_allowed + 1):
    try:

        word = input('Веедіть слово/набір символів, в якому будемо шукати символ:')
        symp_prompt = f'Введіть порядковий номер символу, який треба витягти зі слова (ціле число від 1 до {len(word)}):'
        symb_num = int(input(symp_prompt))
        print('-'* 40)

        # Made this part for rare words with 10 and more chars, while risking violation of YAGNI.
        # Tertiary operator it is, because it fits in one row
        # Just for lulz I made it work for big numbers such as 111 and 1000013 as well
        num_suffix = 'th' if symb_num % 10 not in {1, 2, 3} or symb_num % 100 in {11, 12, 13} else ('st', 'nd', 'rd')[(symb_num - 1) % 10]
        print(f"The {symb_num}{num_suffix} symbol in the word '{word}' is '{word[symb_num - 1]}'")
        break

    except ValueError:
        print('Помилка типу даних: введіть слово/набір символів, а також ціле число')

    except IndexError:
        print('Помилка у номері символу: номер символу, має бути не більшим за довжину слова/введеного набору символів')

    if attempt_count >= max_attempts_allowed:
        print('Спроби закінчились. Запустіть код із самого початку')
        break
    elif attempt_count == max_attempts_allowed - 1:
        attempt_count += 1
        print('-' * 40)
        print(f'Це Ваша остання спроба, {attempt_count} з {max_attempts_allowed} дозволених')
    else:
        attempt_count += 1
        print('-' * 40)
        print(f'Спроба {attempt_count} з {max_attempts_allowed} дозволених')
