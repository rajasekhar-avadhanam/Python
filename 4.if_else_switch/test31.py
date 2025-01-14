x = 10
y = 20

'''

if x<y:
	print('min value',x)
else:
	print('min value',y)

'''

print('min value:', x if x<y else y)

max = x if x>y else y

print('max value:', max)