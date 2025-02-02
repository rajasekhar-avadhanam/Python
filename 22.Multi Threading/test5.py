import threading

def first_th():
	for i in range(20):
		print(i)


def second_th():
	for i in range(40,60):
		print(i)

a1 = threading.Thread(target = first_th) #thread object
b1 = threading.Thread(target = second_th) #has-a
a1.start()
b1.start()
a2 = threading.Thread(target = first_th)
b2 = threading.Thread(target = second_th)
a2.start()
b2.start()