# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
# отсортированный массивы.

import random

def merge(array):
	left = []
	right = []

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

	sort = unite(left, right)

	return sort


def unite(lst1, lst2):
	res = []
	while len(lst1) > 0 and len(lst2) > 0:
		if lst1[0] <= lst2[0]:
			res.append(lst1[0])
			lst1.pop(0)
		else:
			res.append(lst2[0])
			lst2.pop(0)
	if len(lst1) > 0:
		res.extend(lst1)
	if len(lst2) > 0:
		res.extend(lst2)

	return res


arr = [round(random.uniform(0, 50), 2) for i in range (10)]
print(arr)

sort = merge(arr)
print(sort)




