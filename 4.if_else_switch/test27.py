def test(arg1):
	def c1():
		print('i am from c1')
		print('i am from c1')
	def c2():
		print('i am from c2')
		print('i am from c2')
	def c3():
		print('i am from c3')
		print('i am from c3')
	d1 = {
	1:c1,
	2:c2,
	3:c3
	}
	d1.get(arg1)()

test(2)

'''

in python we do not have switch case, we can achieve
swicth case functionlaity using outer function,inner
function and dictionaries.

'''
