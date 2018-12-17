# 5. Пользователь вводит две буквы. 
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string


keys = [i for i in range (1, 27)]
values = [i for i in string.ascii_lowercase]

d = dict(zip(values, keys))

first_letter = input('Введите первую букву: ')
second_letter = input('Введите вторую букву: ')

first_value = int(d[first_letter])
second_value = int(d[second_letter])

distance = abs(first_value - second_value) - 1

print('Первая буква на позиции: ', first_value, ', вторая на позиции: ', second_value)
print('Количество букв между ними: ', distance)