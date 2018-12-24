# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр 
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

number = input('Введите число: ')
n = len(number)
number = int(number)

for i in range (1, n + 1):
	value = int(number%10)
	print(value, end = '')
	number = (number - value)/10
