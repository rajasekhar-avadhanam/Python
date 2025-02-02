import re

#\s other than white spaces
m1 = re.finditer('\S','Java1.8 & python3.0 are most widely using versions @ world_wide')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())