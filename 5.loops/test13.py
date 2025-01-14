print('begin')
for i in [123, 456, 10, 'abc', True, 'test']:
	print('loop begin with an index as',i)
	if i == 'abc':
		continue 
		print('end of loop')
	print('loop end with an index as',i)
print('end')
