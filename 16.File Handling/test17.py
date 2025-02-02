import pickle # serialization and de-serialization

#serialization----state or values writing into the file system in binary format.

f1 = open('hello10.txt','wb')
i = 20
pickle.dump(i,f1) # dump----
f1.close()

#de-serilaization
f2 = open('hello10.txt','rb')
j = pickle.load(f2) #load----
f2.close()

print(j)