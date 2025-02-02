i = 10/0
try:
	print(1)
	print(2)
except ZeroDivisionError as msg:
	print(3,type(msg))
finally: # once control enter into try block only then finally will execute.
	print('from finally')
print(4)