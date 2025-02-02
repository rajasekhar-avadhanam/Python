import json
data = {"firstName":"abc",
        "lastName":"B",
		"age": 22,
		"weight":55.6,
		"address":{"houseNo":"123",
		"streetname":"strname"},
		"city":"panama"
}
print(type(data),data)
with open('d1.json','w') as f1:
	json.dump(data,f1)

with open('d1.json','r') as f2:
	x= json.load(f2)
print(type(x),x)