# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string


keys = [i for i in range (1, 27)]
values = [i for i in string.ascii_uppercase]

d = dict(zip(keys, values))

value = int(input('Введите порядковый номер буквы от 1 до 26: '))
letter = d[value]

print('Это буква ', letter)