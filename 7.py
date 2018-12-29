# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

LENGTH = 10
START = 1
STOP = 100

l = [random.randint(START, STOP) for _ in range (0,LENGTH)]
print('Сгенерированный список: ', l)

minimum = 100
posmin = 0
next_minimum = 100

for i in range (0, len(l)):
	if l[i] <= minimum:
		minimum = l[i]
		posmin = i

for i in range (0, len(l)):
	if l[i] <= next_minimum and i != posmin:
		next_minimum = l[i]

print('Минимальный элемент равен ', minimum)
print('Второй минимальный элемент равен ', next_minimum)
