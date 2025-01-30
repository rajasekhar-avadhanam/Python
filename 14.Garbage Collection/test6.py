import sys

class A:
	pass

a1 = A()
print(sys.getrefcount(a1))
a2 = a1
print(sys.getrefcount(a1))
a3 = a2
print(sys.getrefcount(a1))
a4 = a3
print(sys.getrefcount(a1))
print('--------------')

a1 = None
a2 = None
print(sys.getrefcount(a4))
print('--------------')
a3 = None
print(sys.getrefcount(a4)) 
a4 = None
print(sys.getrefcount(a4)) # this will give junk value
#print(sys.getrefcount(self)) # we can write self only in function we can not write it in main stack