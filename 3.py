# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный 
# элементы.

import random

START = 1
STOP = 100

l = [random.randint(START, STOP) for _ in range (0,LENGTH)]
print('Оригинальный список: ', l)
posmax = 0
posmin = 0
lmax = 0
lmin = 100

for i in range (0, len(l)):
	if l[i] >= lmax:
		lmax = l[i]
		posmax = i
	elif l[i] <= lmin:
		lmin = l[i]
		posmin = i

print('Минимальный элемент списка имеет индекс ',posmin, ' и равен ', lmin)
print('Максимальный элемент списка имеет индекс ', posmax, ' и равен ', lmax)

l.pop(posmax)
l.insert(posmax, lmin)
l.pop(posmin)
l.insert(posmin, lmax)


print('Поменяли их местами: ', l)
