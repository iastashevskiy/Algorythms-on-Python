
from collections import Counter
from collections import OrderedDict

class DerNode:
	def __init__(self, value, left = None, right = None):
		self.value = value
		self.left = left
		self.right = right
		
		

def huffman(statement):
	statement = Counter(statement)
	statement = OrderedDict(sorted(statement.items(), key = lambda t: t[1]))
	print(statement)
	order = list(statement.values())
	value = list(statement.keys())
	print(order)
	print(value)

	while len(order) > 1:
		m = 1
		val = int(order[0]) + int(order[1])
		lft = value[0]
		rght = value[1]
		Node  = DerNode(val, lft, rght)
		order.pop(1)
		order.pop(0)
		order.append(val)
		order.sort()
		value.pop(1)
		value.pop(0)
		value.insert(order.index(val), val)
		m += 1
		print(order)
		print(value)


	
	return statement



statement = input('Введите слова: ')

print(huffman(statement))

