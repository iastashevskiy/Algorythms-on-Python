# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его 
# значение и позицию в массиве.

import random
import sys

def show_size(x, level=0):
	total_size = 0
	for i in x:
		total_size += sys.getsizeof(x[i])
		if hasattr(i, '__iter__'):
			if hasattr(i, 'items'):
				for key, value in i.items():
					show_size(key, level + 1)
					show_size(value, level + 1)
			elif not isinstance(i, str):
				for item in i:
					show_size(item, level + 1)
	return total_size

LENGTH = 10
START = -100
STOP = 100


lst = [random.randint(START, STOP) for _ in range (0,LENGTH)]
print(lst)

srtd = lst.copy()
srtd.sort()

queue = len(srtd)

while srtd[queue - 1] > 0:
	srtd.pop()
	queue = len(srtd)

position = lst.index(srtd[queue - 1])


print('Максимальный отрицательный элемент имеет индекс ', position, ' и равен ', srtd[queue - 1])

global_variables = globals()
local_variables = locals()
print('Использовано памяти: ', show_size(global_variables) + show_size(local_variables))