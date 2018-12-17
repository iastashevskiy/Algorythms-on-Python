# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает 
#свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', 
# то вводятся эти символы. Программа должна вывести на экран любой символ алфавита 
# от 'a' до 'f' включительно.

import string
import random

keys = [i for i in range (1, 27)]
values = [i for i in string.ascii_lowercase]
d = dict(zip(values, keys))
d1 = dict(zip(keys, values))

lower = input('Введите нижнюю границу: ')
upper = input('Введите верхнюю границу: ')

if lower in string.ascii_lowercase and upper in string.ascii_lowercase:
	start = int(d[lower])
	stop = int(d[upper])
	random_key = random.randint(start, stop)
	random_letter = d1[random_key]
	print('Случайная буква: ', random_letter)
else:
	integer = random.randint(int(lower), int(upper))
	number = random.uniform(int(lower), int(upper))
	print('Случайное число: ', number, '. Случайное целое число: ', integer)