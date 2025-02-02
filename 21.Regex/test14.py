import re

#\D represents char other than digits as a pattern
m1 = re.finditer('\D','java1.8 & python3.0 are most widely using versions @ worldwide')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())