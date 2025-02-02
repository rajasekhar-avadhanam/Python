def my_generator():
	print('gen')  #it is not returning a value we have to use for loop to print values from generator.
	yield 1

def f1():
	print('f1')

def f2():
	print('f2')
	return 100

print(type(my_generator))
print(type(f1))
print(type(f2))
print(type(my_generator()))
print(type(f1()))
print(type(f2()))