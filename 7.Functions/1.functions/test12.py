# the parameter can have a default value
# and if we supply a value then this default value will be
# overridden

def test1(arg1 = 5):
	print('from test1:', arg1)

test1()
test1(100)
test1('abc')