# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

def get_digit_summ(value):
	n = len(value)
	value = int(value)
	summ = 0
	for i in range (1, n + 1):
		summ = summ + value%10
		value = (value - value%10)/10

	return summ

number = input('Введите число. Для выхода введите 0: ')
biggest_digits_summ = 0
biggest_number = 0

while number != '0':
	new_digits_summ = get_digit_summ(number)
	if new_digits_summ > biggest_digits_summ:
		biggest_digits_summ = new_digits_summ
		biggest_number = number
		number = input('Введите новое число. Для выхода введите 0: ')
	else:
		number = input('Введите новое число. Для выхода введите 0: ')
else:
	print('Число с наибольшей суммой цифр: ', biggest_number)
	print('Его сумма цифр равна ', biggest_digits_summ)






