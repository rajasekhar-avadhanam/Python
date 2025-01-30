# constructor over-loading is not possibe in python
# though it allows syntactically we have to use last defined constructor only.

class A:
	def __init__(self):
		print('first constructor')
	def __init__(self,i):
		print('2nd constructor')
	def __init__(self,i,j):
		print('3rd consturctor')

#a1 =A()
#a2 = A(20)
a3 = A(1,20)