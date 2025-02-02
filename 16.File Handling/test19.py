import pickle
class A:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def __str__(self): # when we print ref variable str function executes
		return str(self.x)+","+str(self.y)
	
f1 = open('hello12.txt','wb')
a1 = A(10,20)
a2 = A(100,200)

pickle.dump(a1,f1)
pickle.dump(a2,f1)

f1.close()

f2 = open('hello12.txt','rb')
a3 = pickle.load(f2)
a4 = pickle.load(f2)
f2.close()

print(a3)
print(a4)