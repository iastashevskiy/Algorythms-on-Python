# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
# отсортированный массивы.

import random

def merge(array):
	left = []
	right = []
	sort = []
	if len(array) <= 1:
		return array
	else:
		middle = round(len(array)/2)
		for i in range (0, middle):
			left.append(array[i])
		for i in range (middle, len(array)):
			right.append(array[i])
		left = merge(left)
		right = merge(right)

	return left, right





arr = [round(random.uniform(0, 50), 3) for i in range (10)]

print(arr)
sort = merge(arr)
print(sort[0])
print(sort[1])
