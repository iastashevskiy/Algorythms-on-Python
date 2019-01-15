# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random
import cProfile

def test_function():
	LENGTH = 10000
	START = 1
	STOP = 1000000000

	lst = [random.randint(START, STOP) for _ in range (0,LENGTH)]
	# print('Сгенерированный список: ', l)

	minimum = STOP
	posmin = 0
	next_minimum = STOP

	for i in range (0, len(lst)):
		if lst[i] <= minimum:
			minimum = lst[i]
			posmin = i

	for i in range (0, len(lst)):
		if lst[i] <= next_minimum and i != posmin:
			next_minimum = lst[i]
	return minimum, next_minimum




# 100 loops, best of 3: 859 usec per loop - LENGTH = 100
# 100 loops, best of 3: 8.62 msec per loop - LENGTH = 1000
# 100 loops, best of 3: 85.3 msec per loop - LENGTH = 10000

# cProfile.run('test_function()')
# 1    0.000    0.000    0.005    0.005 uno.py:7(test_function) - LENGTH = 100
# 1    0.001    0.001    0.041    0.041 uno.py:7(test_function) - LENGTH = 1000
# 1    0.006    0.006    0.411    0.411 uno.py:7(test_function) - LENGTH = 10000

# Вывод: сложность алгоритма - О(n). Недостаток алгоритма: массив анализируетя дважды.
# Возможно ускорение в два раза при нахождении значений за одну итерацию
