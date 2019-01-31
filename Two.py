# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
# отсортированный массивы.

import random

def merge(array):
	left = []
	right = []
	res = []

	if len(array) <= 1:
		return array

	middle = round(len(array)/2)
	for i in range (0, middle):
		left.append(array[i])
	for i in range (middle, len(array)):
		right.append(array[i])
	
	# print(left)
	# print(right)
	# print('-----------------------------------------------')
	left = merge(left)
	right = merge(right)

	while len(left) > 0 and len(right) > 0:
		if left[0] <= right[0]:
			res.append(left[0])
			left.pop(0)
		else:
			res.append(right[0])
			right.pop(0)
			
	if len(left) > 0:
		res.extend(left)
	if len(right) > 0:
		res.extend(right)


	return res



arr = [round(random.uniform(0, 50), 2) for i in range (10)]
print(arr)

sort = merge(arr)
print(sort)




