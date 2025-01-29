'''

A
B B
C C C
D D D D
E E E E E
F F F F F F
G G G G G G G

'''


'''
char ='A'
print(char)
print(chr(ord(char)+1))
print(chr(ord(char)+2))
print(chr(ord(char)+3))

ch ='f'
print(chr(ord(ch)+1))
print(chr(ord(ch)+2))
print(chr(ord(ch)+3))
print(chr(ord(ch)+4))

'''


fis_char = 'A'
for row in range(0,7):
	for col in range(0,row+1):
		print(chr(ord(fis_char)+row),' ',end='')
	print()