'''
to remove the duplicates from the list/tupple we can just
convert the list/tupple to the set and then again convert the
set into list/tupple.
'''

x = [10,20,40,10,20,30]
print(x)
y = set(x)
print(y)
x = list(y)
print(x)
print(type(x))