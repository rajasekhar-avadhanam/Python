#First 10 prime Numbers

x = int(input('enter first number'))
y = int(input('enter second number'))
z = 2
flag = True
while x <= y:
	while(z <= (x/2)):
		if(x %z == 0):
			flag = False
			break
		z+= 1
	if flag:
		print(x,end = ',')
	x+=1
	z=2
	flag = True
