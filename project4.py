data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
numbers = []
letters = []

for item in data_tuple:
    if type(item) == str:
        letters.append(item)
    else:
        numbers.append(item)

        print("После разделения:")
        print("letters", letters)
        print("numbers", numbers)

numbers.remove(6.13)
numbers.remove(True)
letters.append(True)
numbers.insert(1, 2)

print("\n Изменение в шаге 3:")
print("letters", letters)
print("numbers", numbers)

numbers.sort()
letters.reverse()

if 'T' in letters:
    letters[letters.index('T')] = 't' 
if 'C' in letters:
    letters[letters.index('C')] = 'c'
    
    letters.remove(True)

    print("\n После сортировки и реверса")
    print("letters",letters)
    print("numbers", numbers)

    letters = ['t', 'e', 'c', 'h']

    print("\n Составленное слово из букв:")
    print ("".join(letters))

    letters_turple = tuple(letters)

    print("\n Финальные результаты:")
    print("letters",letters )