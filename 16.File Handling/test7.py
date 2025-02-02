f1 = open('hello2.txt','r')
line = f1.readline() #1st line
while line:
	print(line)
	line = f1.readline()
f1.close()
