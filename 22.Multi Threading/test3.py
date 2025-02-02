import threading

class A(threading.Thread):
	def run(self):
		for i in range(20):
			print(i)

class B(threading.Thread):
	def run(self):
		for i in range(40,60):
			print(i)

a1 = A()
b1 = B()
a1.start()
b1.start()

a2 = A()
b2 = B()
a2.start()
b2.start() #start() internally calling run() from class A/class B