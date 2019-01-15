
import math
import cProfile

def prime(n):
	lst = [2]
	MAX_VALUE = 1000000000

	for i in range (2, int(math.sqrt(MAX_VALUE))):
		if len(lst) == n:
			break
		else:
			prime = True
			for j in lst:
				if i%j == 0:
					prime = False
	
			if prime == True:
				lst.append(i)
		
	return lst[n-1]

# 100 loops, best of 3: 79 usec per loop, n = 10
# 100 loops, best of 3: 1.7 msec per loop, n = 50
# 100 loops, best of 3: 7.63 msec per loop, n = 100
# 100 loops, best of 3: 276 msec per loop, n = 500

# cProfile.run('prime(500)')

# 1    0.000    0.000    0.000    0.000 dos.py:5(prime), n = 10
# 1    0.003    0.003    0.004    0.004 dos.py:5(prime), n = 50
# 1    0.069    0.069    0.071    0.071 dos.py:5(prime), n = 100
# 1    0.282    0.282    0.295    0.295 dos.py:5(prime), n = 500