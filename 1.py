# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import cProfile

def test_function():
	LENGTH = 10000
	START = 1
	STOP = 1000000000

	l = [random.randint(START, STOP) for _ in range (0,LENGTH)]
	# print('Сгенерированный список: ', l)

	minimum = STOP
	posmin = 0
	next_minimum = STOP

	for i in range (0, len(l)):
		if l[i] <= minimum:
			minimum = l[i]
			posmin = i

	for i in range (0, len(l)):
		if l[i] <= next_minimum and i != posmin:
			next_minimum = l[i]
	return minimum, next_minimum

cProfile.run('test_function()')

minimum = test_function()

 # print('Минимальный элемент равен ', minimum)
 # print('Второй минимальный элемент равен ', next_minimum)

print (minimum)
