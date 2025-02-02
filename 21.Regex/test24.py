import re
import re
s1 = 'a1aabcaaa234aaaahelloaaaaatest'
print('source:',s1)
m1 = re.finditer('a{2,4}',s1) #{2,4} range from 2-4
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())