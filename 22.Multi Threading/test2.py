import threading

class A(threading.Thread): #thread class in super class to A
	def run(self): # run funtion from Thread class we are over riding the run function
		for i in range(40):
			print(i)

class B(threading.Thread):
	def run(self):
		for i in range(40,80):
			print(i)

a1 = A()
b1 = B()
a1.start()
b1.start()