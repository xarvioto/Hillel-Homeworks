# 2. Вести з консолі строку зі слів за допомогою input() (або скористайтеся константою). Напишіть код, який визначить
# кількість слів, в цих даних.

# the shortest version I can come up with. It does the job, not more than task demands.
# It might be too short to be pleasant. I commented it.

# print(len(input('Прошу ввести сюди строки, а я порахую скільки в цій строці слів:').split()))

# Here is a little longer version. I wonder if the good one is somewhere in the middle.

list_of_words = input('Прошу ввести сюди строку, а я порахую скільки в цій строці "слів":').split()
len_of_words = len(list_of_words)
if len_of_words % 10 not in {1, 2, 3, 4} or len_of_words % 100 in {11, 12, 13, 14}:
    word_with_case = ' слів'
elif len_of_words % 10 == 1:
    word_with_case = ' слово'
else:
    word_with_case = ' слова'

print(f'у Вашій строці {len_of_words}{word_with_case}')