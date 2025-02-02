import threading
class A:
	def first_th(self):
		for i in range(20):
			print(i)

class B:
	def second_th(self):
		for i in range(40,60):
			print(i)

a1 = threading.Thread(target = A().first_th) #thread object
b1 = threading.Thread(target = B().second_th) #has-a
a1.start()
b1.start()
a2 = threading.Thread(target = A().first_th)
b2 = threading.Thread(target = B().second_th)
a2.start()
b2.start()