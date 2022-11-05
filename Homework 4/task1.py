# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні
# літери підряд.

vowels_set = {'a', 'e', 'u', 'i', 'o'}

while True:
    input_string = input('Please enter some string to check:')
    if not input_string:
        print('Error: a string should be not empty. Please, try entering something again')
    else:
        break

list_of_words = input_string.lower().split(' ')


result_word_counter = 0

for word in list_of_words:
    vowel_counter = 0
    for char in word:
        if char in vowels_set:
            vowel_counter += 1
        else:
            vowel_counter = 0

        if vowel_counter >= 2:
            result_word_counter += 1
            break

print('-' * 40)
print(f'In your string "{input_string}"\n'
      f'there are ----> {result_word_counter} <---- words\n'
      f'containing two chars in a row from {vowels_set}')
