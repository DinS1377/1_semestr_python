# Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы. Отобразить исходный и
# получившийся словарь. Использовать for, range.

key = 0
value = 0
numbers = {}

#создание исходного словаря
for i in range(0, 7):
    key = i
    value = i*i*i
    numbers[key] = value

print(f'исходный словарь:{numbers}')

#удаление элементов
del numbers[0]
del numbers[6]


print(f'получившийся словарь: {numbers}')

