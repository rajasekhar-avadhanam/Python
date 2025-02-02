import re

#\s other than white spaces
m1 = re.finditer('a+','a1aaabcaaa234aaaahelloaaaaatest')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())