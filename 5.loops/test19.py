for i in range(5):
	print('i am from outer loop begin',i)
	for j in range(10,12):
		print('i am from inner loop begin',i,j)
		if i==3:
			break
		print('i am from inner loop end',i,j)
	print('i am from the outer loop end',i)


'''
in python we can not break or continue the outer loop
by writing break/continue in the inner loop.

But we can control the outer loop using the
continue/break written in inner loop in JAVA.

In java we have concept called labelled loops wehere we
can assign names to loops and use them in inner loops.


'''