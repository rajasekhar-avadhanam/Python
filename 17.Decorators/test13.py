def decorator(f1):
	def original_with_dec():
		print('before')
		f1()
		print('after')
	return original_with_dec

@decorator
def original():
	print('from original')

original()
original()
original()
original()
original()



