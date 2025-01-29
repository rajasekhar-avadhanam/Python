x = [10,200,15,35,40,200,150,40,65]

print(x)

def isEven(a):
	print(a)
	return a % 2 == 0

for a in x:
	if(isEven(a)): # isEven is a function that we defined
		print(a,"is even")
	else:
		print(a,"is odd")