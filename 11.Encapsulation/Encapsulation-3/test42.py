# method overloading, same method name but with different
#no.of arguments

class A:
	def test1(self):
		print('first test1')
	def test1(self,i):
		print('2nd test1')
	def test1(self,i,j):
		print('3rd test1')

a1 = A()

#a1.test1()
#a1.test1(10)
a1.test1(10,20)

