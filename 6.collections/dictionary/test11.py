#use pop supplied with key to remove an element

# https://docs.python.org/3/library/function.html
x = {"K1": "hello","K2":True,"K3":4.5,"abc":56,"xyz":677,80: False}
print(x)
x.pop('abc')
print(x)
x.pop('K3')
print(x)