class A:
	def __init__(self,p):
		self.x = p #1st way

	def f1(self,i):
		print('from f1')
		self.i = i #2nd way

	def f2(self,m):
		print("from f2")
		self.j = m


a1 = A(20)
a1.y = 2000 #3rd way
print(a1.__dict__)
a1.z = 'abc'
a1.f1(10)
print(a1.__dict__)
a1.f2(20)
a1.n = 9.5
print(a1.__dict__)