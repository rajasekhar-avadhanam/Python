class MyDec:
	def __init__(self,f1):
		self.f1 = f1
	def __call__(self): #decorator function
		print(1)
		self.f1()
		print(2)
	
def function1():
	print('i am from function1')

function1()
print('----------')

m1 = MyDec(function1)
m1() # by calling m1 we are executing __call__ from the class.