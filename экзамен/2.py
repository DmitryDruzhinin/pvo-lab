vowels = ('а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я')
consonants = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')


print('введите фамилию')
surname = input().lower()
print('введите имя')
name = input().lower()
print('введите отчество')
otchestvo = input().lower()

vowel_count = 0
consonant_count = 0
otchestvo_count = 0

for char in surname:
    if char in vowels:
        vowel_count += 1

for char in name:
    if char in consonants:
        consonant_count += 1

for char in otchestvo:
    if char in consonants:
        otchestvo_count += 1
    if char in vowels:
        otchestvo_count += 1


res = (vowel_count * consonant_count * otchestvo_count) % 10 + 1
print(res)
