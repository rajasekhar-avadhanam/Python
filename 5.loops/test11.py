print('begin')
list1=[123, 456, 10, 'abc', True, 'test']
for i in list1:
	print('loop begin with an index as',i)
	if i == 'abc':
		break 
	print('loop end with an index as',i)
print('end')

'''
when ever break is executed the entire loop will
be termiated and the control will come out from the
loop.

'''