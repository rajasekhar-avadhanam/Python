class A:
	class B:
		def f1(self):
			print('from B.f1')
	def f2(self):
			print('from A.f2')

a1 = A()
#a1.f1()
a1.f2()