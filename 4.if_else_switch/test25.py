def f1():
	print(1)
	def f11():
		print(2)
		print(2)
		print(2)
	print(3)
	f11()
	print('2nd f11')
	f11()

f1()
print('-----------')
f1()
print('-----------')
#f11()---> we will get error as it is inside f1()

'''
how to call the inner function---
we have to call the inner funtion inside from
outer fnction.
'''