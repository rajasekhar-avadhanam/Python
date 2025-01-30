from abc import ABC, abstractmethod   #abc--abstrcat base class
class X:   #ABC---class name, abstractmethod--annotation name.
	pass

class Y(ABC):
	pass


class Z:
	@abstractmethod
	def f1():
		print('some thing')

class P(ABC):
	@abstractmethod
	def f1(self):
		print('from P.f1')

# we can create object to X,Y,Z but we can not create
#object to P because it is an abstract class.

#what is an abstract class---A class has to be sub-class
#to ABC and it should have atleast on abstr		act method.

ref1 = X()
ref2 = Y()
ref3 = Z()
#Z.f1() if self is not given

#ref4 = P()
print('done')