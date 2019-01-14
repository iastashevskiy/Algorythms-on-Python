
import math

def prime():
	lst = [2]
	for i in range (2, 10):
		for j in lst:
			if i%j != 0:
				lst.append(i)
				continue
	return lst

l = prime()
print (l)