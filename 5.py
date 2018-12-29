# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его 
# значение и позицию в массиве.

import random

LENGTH = 10
START = -100
STOP = 100

l = [random.randint(START, STOP) for _ in range (0,LENGTH)]
print(l)

lmax = -100
posmax = 0

for i in range (0, len(l)):
	if l[i] >= lmax and l[i] < 0:
		lmax = l[i]
		posmax = i

print('Максимальный отрицательный элемент имеет индекс ', posmax, ' и равен ', lmax)