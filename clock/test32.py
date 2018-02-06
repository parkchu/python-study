name = ['parkchu', 'javajigi', 'alex', 'pikachu', 'miso']

for x in name:
    print(x)

print('the names are ', 'parkchu', 'javajigi', 'alex', 'pikachu', 'miso')
print('Replace one name.')
changename = input()
print('which one? (1-5)')
number = input()
number = int(number)
number = number - 1

del name[number]
name.insert(number, changename)

for y in name:
    print(y)

    






