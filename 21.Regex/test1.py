import re

p1 = re.compile('a')   #pattern definition
m1 = p1.finditer('abcahelloatesta123')
#print(m1)

for exp in m1:
	print(exp.start())