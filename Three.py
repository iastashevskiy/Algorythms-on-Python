# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две 
# равные части: в одной находятся элементы, которые не меньше медианы, в другой – 
# не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это
#  слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

START = random.randint(-100, 0)
STOP= random.randint(0,100)
SIZE_M = random.randint(2, 10)

arr = [round(random.uniform(START, STOP), 2) for i in range (2*SIZE_M + 1)]
# arr = [1,2,3,1,1,3,7] - на этом тестировал повторяющиеся элементы
print(arr)

median = arr.copy()

while len(median) > 1:
	max = START
	min = STOP
	for i in range(0, len(median)):
		if median[i] > max:
			max = median[i]
		if median[i] < min:
			min = median[i]
	median.remove(max)
	median.remove(min)

print('Медиана массива: ', median[0])


