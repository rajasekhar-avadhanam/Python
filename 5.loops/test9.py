print('begin')
for i in range(10):
	print('loop begin with an index as',i)
	if i >= 5:
		continue 
	print('loop end with an index as',i)
print('end')