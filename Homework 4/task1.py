# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні
# літери підряд.

vowels_set = {'a', 'e', 'u', 'i', 'o'}

input_string = ''

while not input_string:
    input_string = input('Please enter some string to check:')
    if not input_string:
        print('Error: a string should be not empty. Please, try entering something again')

list_of_words = input('Please enter some string to check:').lower().split(' ')

vowel_counter = 0
result_word_counter = 0

for word in list_of_words:
    for char in word:
        if char in vowels_set:
            vowel_counter += 1
            if vowel_counter >= 2:
                result_word_counter += 1
                vowel_counter = 0
                break
        else:
            vowel_counter = 0

print('-' * 40)
print(f'In your string "{input_string}"\n'
      f'there are ----> {result_word_counter} <---- words\n'
      f'containing two chars in a row from the set {vowels_set}')
