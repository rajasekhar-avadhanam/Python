print('begin')
for i in [123, 456, 10, 'abc', True, 'test']:
	print('loop begin with an index as',i)
	if i == 'abc':
		break 
		print('end of loop')
	print('loop end with an index as',i)
print('end')

'''

--->after break in line-5, ln 6,7 wont execute.

--->in general break/continue will be the last statement
in the current block but in python we can give break
at any where.


--->when ever break is executed the entire loop will
be termiated and the citrol will come out from the
loop.

'''