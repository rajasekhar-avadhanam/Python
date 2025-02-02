import threading

def test1():
	for i in range(50):
		print(i,threading.current_thread().name)


t1 = threading.Thread(target = test1)
t1.start()

t1.join() #once the t1(child thread) is completely executed only then ain thread will execute.

print('from main stack',threading.current_thread().name)