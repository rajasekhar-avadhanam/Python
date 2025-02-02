import json
data = [{"firstName":"abc",
        "lastName":"B",
		"age": 22,
		"weight":55.6,
		"address":{"houseNo":"123",
		"streetname":"strname"},
		"city":"Panama"
},
{"firstName":"xyz",
        "lastName":"B",
		"age": 24,
		"weight":65.6,
		"address":{"houseNo":"456",
		"streetname":"strname2"},
		"city":"Panama"
}]
print(type(data),data)
print(type(data[0]),data[0])
print('------------------------')
with open('d2.json','w') as f1:
	json.dump(data,f1)

with open('d2.json','r') as f2:
	x= json.load(f2)
print(type(x),x)
print(type(x[0]),x[0])