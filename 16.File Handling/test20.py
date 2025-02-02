import json  #javascript object notation

data = '{"attr1":"hello","attr2":"test"}'
s1 = json.loads(data)
print(s1)