import re

#\W represents other than word chars(alpha(lower and upper),numeric and _ considers in 'w').
m1 = re.finditer('\W','Java1.8 & python3.0 are most widely using versions @ world_wide')
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())