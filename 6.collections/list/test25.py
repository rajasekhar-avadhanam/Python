x = [10,3.5,'abc',True,300,4.5,'xyz',False]
y = list(x) # depp copy
print(x)
print(y)
print('-------------')
x[5] = 7000
print(x)
print(y)