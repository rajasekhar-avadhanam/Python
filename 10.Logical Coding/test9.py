base_char ='A'

for row in range(0,8):
	for col in range(0,row+1):
		print(chr(ord(base_char)+col),' ',end='')
	print()