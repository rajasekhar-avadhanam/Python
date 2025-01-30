from abc import ABC, abstractmethod   #abc--abstrcat base class

class P(ABC):
	@abstractmethod
	def f1(self):
		print('P.f1')

class Q(P): # it is also an abstrcat class from P class
	pass

class R(P): #it is also an abstract class from P class but it is implementing the function from P class so we can create an object.
	def f1(self):
		print('R.f1()')


#ref1 = P()
#ref2 = Q()
ref3 = R()
#ref2.f1()
ref3.f1()
print('done')