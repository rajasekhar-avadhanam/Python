class A:
	def __init__(self):
		print('constructor is executing')

	def __del__(self):
		print('destrctor is executing')
	
a1 = A()
a1 = None # objet with out any reference is call dead/abandoned object
a2 = A()
a2 = None
a3 = A()
print('done')