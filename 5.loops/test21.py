status = False
for i in range(5):
	print('i am from the outer loop begin', i)
	for j  in range(10,12):
		print('i am from inner loop begin',i,j)
		if j == 10:
			status =True
			continue
		print('i am from inner loop end',i,j)

	if status:
		break;
	print('i am from the outer loop end',i)