class Test:
	i = 100
	j = 'abc'

print(Test.i)
print(Test.j)
t1 = Test()
t2 = Test()
t3 = Test()

print(t1.i,t1.j)
print(t2.i,t2.j)
print(t3.i,t3.j)

Test.i = 5000
Test.j = 'xyz'

t1.i = 10
t1.j = 20
t2.i = False
t2.j = 6.7
t3.i = 60000
t3.j = True

print(t1.i,t1.j)
print(t2.i,t2.j)
print(t3.i,t3.j)