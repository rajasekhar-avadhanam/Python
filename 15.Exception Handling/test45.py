i = input('enter a number')
print(1)
try:
	print(2)
	j = int(i)
	print(3)
	k = j/(j-9)
	print(4)
	list = [10,20,30,40,50]
	m = list[j]
	print(5)
except ValueError:
	print('from ValueError')
except ZeroDivisionError:
	print('from ZeroDivisionError')
finally: #it is guranteed to execute in every run
	print('i am from finally block')
print(5)