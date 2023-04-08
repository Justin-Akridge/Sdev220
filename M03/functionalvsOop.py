#functional example

def subtract(a, b):
	return a - b

def division(a, b):
	return a // b

print(subtract(5, 2))
print(division(4, 2))


#OOP example

class do_math:
	def __init__(self, val1, val2):
		self.val1 = val1
		self.val2 = val2
	
	def subtract_oop(self):
		return self.val1 - self.val2
	
	def division_oop(self):
		return self.val1 / self.val2

math_instance = do_math(20, 8)
print(math_instance.subtract_oop())
print(math_instance.division_oop())

