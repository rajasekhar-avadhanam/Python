import pickle # serialization and de-serialization

#serialization----state or values writing into the file system in binary format.

f1 = open('hello11.txt','wb')
i = 20
j = 40
pickle.dump(i,f1) # dump----
pickle.dump(j,f1)
f1.close()

f2 = open('hello11.txt','rb')
x = pickle.load(f2)
y = pickle.load(f2)
f2.close()

print(x)
print(y)