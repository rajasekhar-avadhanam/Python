class A:
	def __init__(self):
		print('constructor is executing')
	
	def __del__(self):  # destructor is automatically implemented by garbage collector when there us no ref to an object
		print('destructor is executing')

a1 = A()
a2 = A()
a3 =A()
print('done')