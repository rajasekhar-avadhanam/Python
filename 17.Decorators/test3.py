def outer_func():
	print(1)
	inner_func() # error because calling before declaration.
	print(2)
	def inner_func():
		print(3)
	print(4)

print(5)
outer_func()
print(6)