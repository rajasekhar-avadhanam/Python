class A:
	pass

a1 =A()
a2 =A()

a1.i = 3000
a2.j = 'abc'
a1.k = 'hello'
a2.m = 'hello'

a1.x = a2  # a1 has a2 --> a1 has a relation with a2.
print(a1.__dict__)
print(a2.__dict__)