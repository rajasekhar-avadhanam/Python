import functools

x = [1,20,15,25,4,2]
print(x)

y = functools.reduce(lambda a,b: a+b,x) # so in first case it will add 1+20 and then from second it will take 21 and next element from list which is 15

print(y)