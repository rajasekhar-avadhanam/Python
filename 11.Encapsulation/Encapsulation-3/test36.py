class Address:
	def __init__(self):
		self.house_no = None
		self.street_name = None

class Person:  # person has address(has-a relation)
	def __init__(self):
		self.first_name = None
		self.last_name = None
		self.age = None
		self.address = None


p1 = Person()
p1.first_name = 'vi'
p1.last_name = 'vi'
p1.age = 25

p1.address = Address()
p1.address.house_no = '123'
p1.address.street_name = 'ABC'
print(p1.__dict__,p1.address.__dict__)
