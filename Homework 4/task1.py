# Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран кількість слів, які містять дві голосні
# літери підряд.

vowels_set = {'a', 'e', 'u', 'i', 'o'} # just a mere list of vovels

# intital set of vowels and list of doubled vowels are two different things. Potentially 'vowels -> double vowels'
# should be a separate function, that may double, tripple, or change the set completely. As we don't use functions
# yet, i completely separate the code of processing our vowel set to double so the rest of code does not break if
# vowel set is changed, or processing rule is changed
target_set = {vowel * 2 for vowel in vowels_set} # condition rule, that may be changed anytime


input_string = ''
output_list = []

while not input_string:
    input_string = input('Please enter some string to check:')
    try:
        assert len(input_string) > 0  # In general I suppose, that anything (incl numerical) is a valid string here
    except AssertionError:  # 'AssertionError as ae' would be a YAGNI? because I write a custom error message
        print('Error: a string should be not empty. Please, try entering something again')

# all the next code i could have stuck into else: of try:, but it is read better this way
list_of_words = input_string.split(' ')  # Here i suggest that only space separates the words. Otherwise - split('')
for word in list_of_words:
    for d_vowel in target_set: # naming is still tied to 'double vowels rule', for now, othervise it is harder to comprehend
        if d_vowel in word:
            output_list.append(word)

print('-' * 40)
print(f'In your string "{input_string}"\n'
      f'there are ----> {len(output_list)} <---- words\n'
      f'containing chars from the set {target_set}')
print(f'Check it out by yourself. Here is the list of words that fits:\n {output_list}' if output_list else '-' * 40 )
