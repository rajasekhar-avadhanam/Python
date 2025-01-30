class Address:
	def __init__(self):
		self.house_no = None
		self.street_name = None

class Person:  
	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.age = None
		self.address = None


p1 = Person()
p1.first_name = 'vi'
p1.last_name = 'vi'
p1.age = 25

a1 = Address()
a1.house_no = '123'
a1.street_name = 'abc'
p1.address = a1
print(p1.__dict__,p1.address.__dict__)
