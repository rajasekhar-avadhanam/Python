from collections import Counter
x = [10,3.5,'abc',True,10,4.5,'xyz',False,3.5,10,4.5,False,False]
print(x)
print(Counter(x))
print(x.count(3.5))
print(x.count(10))
print(x.count(False))
print(x.count(4.5))
print(x.count('abc'))
print(x.count('hello'))
