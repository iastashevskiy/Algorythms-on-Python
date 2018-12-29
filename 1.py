# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны 
# любому из чисел в диапазоне от 2 до 9.

numbers = [i for i in range (2,100)]

for i in range (2,10):
	counter = []
	count = 0
	for j in range (0, len(numbers)):
		res = numbers[j]%i
		if res == 0:
			count += 1
	print('Количество чисел кратных ', i, ': = ', count)



