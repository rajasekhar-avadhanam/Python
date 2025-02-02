print(1)
try:
	print(2)
	i = 10 / 0
	print('try ends')
except ZeroDivisionError: # multi-level inheritance in error classes.
	print(3)
except ArithmeticError:
	print(4)
print(5)