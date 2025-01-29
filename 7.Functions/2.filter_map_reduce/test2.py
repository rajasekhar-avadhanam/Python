x = [10,200,15,35,40,200,150,40,65]

print(x)

def calRemainder(a):
	return a % 2 

for a in x:
	if(calRemainder(a) == 0):
		print(a,"is even")
	else:
		print(a,"is odd")