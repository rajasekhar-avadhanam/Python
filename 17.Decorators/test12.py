def original():
	print('from original')

original()

print('---------')

def decorator(f1):
	def original_with_dec():
		print('before')
		#f1()
		print('after')
	return original_with_dec

myDecorator = decorator(original)
myDecorator()