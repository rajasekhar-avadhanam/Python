# if we have duplicate keys the previous key and value pair
# will be replaced by most recent key and value pair.
# one key can refer to only one value.

#x = {"K1": "hello","K1":123}
x = {"K1": "hello","K1":123,"K1":False}
print(x)
