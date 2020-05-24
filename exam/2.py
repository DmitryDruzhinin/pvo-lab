vow = ('а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я')
cons = ('б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ')
surname = input("enter last name: ").lower()
name = input("enter name: ").lower()
patr = input("enter middle name: ").lower()
vow_count = 0
cons_count = 0
patr_count = 0
for char in surname:
    if char in vow:
        vow_count += 1
for char in name:
    if char in cons:
        cons_count += 1
for char in patr:
    patr_count += 1
sum = (vow_count * cons_count * patr_count) % 10 + 1
print("the multiplied number of vowels in the surname, the number of consonants in the name and the number of letters in the middle name, the remainder of dividing the resulting number by 10 and adds one to the result:", sum)
