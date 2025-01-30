class A:
	def test1(self,i,j,k=0):
		print('from test: ',i,j,k)

a1 = A()
a1.test1(10,20)
a1.test1(10,20,30)