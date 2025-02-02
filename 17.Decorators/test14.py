def log_decorator(func):
	def original_with_decorator():
		print('befor executing',func.__name__)
		func()
		print("after execuring",func.__name__)
	return original_with_decorator

def some_tx():
	print('from original')

some_tx()
print('-------------------')

decorated_some_tx = log_decorator(some_tx)
decorated_some_tx()
print('----------------')
some_tx = log_decorator(some_tx)
some_tx()