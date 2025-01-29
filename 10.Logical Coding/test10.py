base_char='A'
for row in range(0,9):
	for col in range(row,-1,-1):
		print(chr(ord(base_char)+col),' ',end='')
	print()