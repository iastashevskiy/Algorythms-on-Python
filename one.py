
# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль 
# за 4 квартала (т.е. 4 отдельных числа)  для каждого предприятия.. Программа должна 
# определить среднюю прибыль (за год для всех предприятий) и вывести наименования 
# предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, 
# чья прибыль ниже среднего.

import collections

QUARTERS = 4
number = int(input('Введите количество предприятий: '))
summary = []
general_average = 0

for i in range (0, number):
	Company = collections.namedtuple('Company'+str(i+1), 'name first second third fourth average')
	raw_data = input('Введите название предприятия и прибыль через запятую: ')
	data = raw_data.split(',')
	average = (int(data[1]) + int(data[2]) + int(data[3]) + int(data[4]))/QUARTERS
	company = Company(data[0], data[1], data[2], data[3], data[4], average)
	summary.append(company)
	general_average = general_average + average

general_average = general_average/number

print('Общая средняя квартальная прибыль равна ', general_average)

# Ниже массив прогоняется дважды с целью красивого вывода результата.
# Буду благодарен, если вы подскажете как можно получить красивый вывод
# за один проход.

print('Компании с прибылью выше среднего:')
for i in range (0, number):
	if summary[i].average > general_average:
		print(summary[i].name, ' : ', summary[i].average)

print('Компании с прибылью ниже среднего:')
for i in range (0, number):
	if summary[i].average <= general_average:
		print(summary[i].name, ' : ', summary[i].average)


