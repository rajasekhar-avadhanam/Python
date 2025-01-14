x = [10,3.5,'abc',True,300,4.5,'xyz',False]
y =x.copy() # deep copy--when changes in original doesnt reflect in y
print(x)
print(y)
print('-------------')
x[5] = 7000
print(x)
print(y)