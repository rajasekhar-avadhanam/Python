import threading
import time

def test1():
	for i in range(10):
		print(i,threading.current_thread().name)
		time.sleep(1)

t1 = threading.Thread(target=test1)
t1.start()

#t1.join()
t1.join(5) #for five seconds child thread will execute for 5 sec after that main and child executes parallely/ if child thread executes before 5 sec after that main will execute.

for i in range(10,20):
	print(i,threading.current_thread().name)
	time.sleep(1)