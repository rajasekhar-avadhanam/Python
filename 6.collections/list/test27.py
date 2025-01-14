x = [10,3.5,'abc',True,300,4.5,'xyz',False]
y = [1,5,'hello',True,301,4.7,'xyz',True]
print(x)
print(y)
print('-----------------------------------------')
y.extend(x)
print(x)
print(y)
print('----------------------------')
z = list(y)
print(x)
print(y)
print(z)