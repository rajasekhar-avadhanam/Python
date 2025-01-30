class A:
	def __init__(self,i,j):
		self.i = i
		self.j = j
	def set_i(self,i):  # setter method---used to set anew value
		self.i = i
	def set_j(self,j):
		self.j = j
	def get_i(self):    # getter method ---used to get the current value
		return self.i
	def get_j(self):
		return self.j

a1 = A(10,20)
a2 = A(30,40)
a3 = A('abc','hello')

print(a1.get_i(),a1.get_j())
print(a2.get_i(),a2.get_j())
print(a3.get_i(),a3.get_j())

a1.set_i(1000)
a2.set_i(2000)
a1.set_j('xyz')
a2.set_j('test')
a3.set_i(6789)
a3.set_j(True)

print(a1.get_i(),a1.get_j())
print(a2.get_i(),a2.get_j())
print(a3.get_i(),a3.get_j())