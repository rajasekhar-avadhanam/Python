import re

#\d represents digit as a pattern and prints the occurences of all digits.
m1 = re.finditer('\d','java8 and python3 are most widely using versions in 2020')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())