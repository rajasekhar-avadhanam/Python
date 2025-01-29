x = [10,200,15,35,40,200,150,40,65]

print(x)

def test1(a):
	return a % 5 ==0
	
def test2(a):
	return a % 10 ==0

y = filter(test1,x)
z = filter(test2,x)

print('all 5 multiples',list(y))
print('all 10 multiples', list(z))