class A:
	def test(self,i=20,j,k=0): #arguments when initiliazed has to be from right to left
		print('from test: ',i,j,k)
	
a1 = A()
a1.test(10)
a1.test(10,20)
a1.test(10,20,30)