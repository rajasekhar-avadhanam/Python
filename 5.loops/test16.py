for i in range(5):
	print('i am from outer loop begin',i)
	for j in range(10,13):
		print('i am from inner loop begin',i,j)
		if j == 11:
			continue
		print('i am from inner loop end',i,j)
	print('i am from the outer loop end',i)

'''
continue only effects the inner loop or the loop 
it is associated with and does not effect the 
outer loop.

'''