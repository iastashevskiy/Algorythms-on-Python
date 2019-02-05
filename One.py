# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный 
# и отсортированный массивы. Сортировка должна быть реализована в виде функции. 
# По возможности доработайте алгоритм (сделайте его умнее).

import random

def bubble(array):
	n = 1
	while n < len(array):
		flag = 0
		for i in range(len(array) - n): # нет необходимости проверять уже отсортированную часть
			if array[i] > array[i + 1]:
				array[i], array[i + 1] = array[i + 1], array[i]
				flag = 1
		if flag == 0:
			break

		n += 1
	return array

START = -100
STOP= 100
LENGTH = 10

arr = [random.randint(START, STOP) for i in range(LENGTH)]

print('Исходный массив: ', arr)
print('Отсортированный массив: ', bubble(arr))