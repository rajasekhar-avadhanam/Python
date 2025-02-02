import re

#\s indices of white spaces
m1 = re.finditer('\s','Java1.8 & python3.0 are most widely using versions @ world_wide')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())