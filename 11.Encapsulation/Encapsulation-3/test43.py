class A:
	def test1():
		print('test1')

	def test2(self):
		print('test2')

A.test1()

a1 = A()
a1.test2()

#a1.test1() #--> a1.test1 --- test1(a1) but test1() doesnt take any argument like self
#A.test2()
#A.test2(a1) #a1.test2()


