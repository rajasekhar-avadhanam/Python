class A:
	def __init__(self): #constructor
		self.i = 20  #a1.i, a1.j
		self.j = 40
	
	def printData(self):  # here self in Arg suggest that it is a member of the object or an instance which will be  reated.
		print(self.i,self.j)

a1 = A()
a1.printData()