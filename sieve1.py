
import cProfile

def sieve(n):

	MAX_VALUE = 1000
	lst = [i for i in range (2, MAX_VALUE)]
	for i in range (2, n):
		for j in lst:
			if j%i == 0 and i != j :
				lst.remove(j)



	return lst[n-1]

# 100 loops, best of 3: 13.2 msec per loop, n = 10
# 100 loops, best of 3: 15.6 msec per loop, n = 50
# 100 loops, best of 3: 17.2 msec per loop, n = 100

# cProfile.run('sieve(100)')

# 1    0.003    0.003    0.017    0.017 sieve1.py:4(sieve), n = 10
# 1    0.005    0.005    0.023    0.023 sieve1.py:4(sieve), n = 50
# 1    0.008    0.008    0.024    0.024 sieve1.py:4(sieve), n = 100

# Вывод: долго генерирует список простых чисел за счет того, что удаляются 
# составные элементы. Если их приравнять 0, то процесс занимает существенно меньшее 
# время. Процесс поиска n-го простого числа практически не меняется в зависимости от 
# выбранного n