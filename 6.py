# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и 
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не 
# включать.

import random

LENGTH = 10
START = 1
STOP = 100

l = [random.randint(START, STOP) for _ in range (0,LENGTH)]
print('Сгенерированный список: ', l)
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

summ = 0

if posmin <= posmax:
	for i in range (posmin + 1, posmax):
		summ = summ + l[i]
else:
	for i in range (posmax + 1, posmin):
		summ = summ + l[i]

print('Минимальный элемент списка имеет индекс ',posmin, ' и равен ', lmin)
print('Максимальный элемент списка имеет индекс ', posmax, ' и равен ', lmax)
print('Сумма элементов между ними равна ',summ)