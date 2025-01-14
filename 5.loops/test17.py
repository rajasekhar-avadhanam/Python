for i in range(5):
	print('i am from outer loop begin',i)
	for j in range(10,12):
		print('i am from inner loop begin',i,j)
		if j==10:
			continue
		print('i am from inner loop end',i,j)
	print('i am from the outer loop end',i)