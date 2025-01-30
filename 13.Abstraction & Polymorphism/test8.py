from abc import ABC,abstractmethod

'''
there is no concept of interface in python but to make
a class type as interface we have to develop a class and all
methods as abstract

here class X we can treat that as interface but it is not
actually an interface.
'''
class X(ABC):            # interface      
	@abstractmethod
	def f1():
		pass

	@abstractmethod
	def f2():
		pass

	@abstractmethod
	def f3():
		pass

	@abstractmethod
	def f4():
		pass

print('done')