i = input('enter a number')
print(1)
try:
	print(2)
	j = int(i)
	print(3)
	k = j / (j - 9)
	print(4)
except ZeroDivisionError:
	print('from ValueError')
except ValueError:
	print('from ZeroDivisionError')
print(5)