import re
s1 = 'a1aabcaaa234aaaahelloaaaaatest'
print('source:',s1)
m1 = re.finditer('a{2,}',s1) #{2,} from 2 -n number of a's
for exp in m1:
	print('search str',exp.group(),'start',exp.start(),'end:',exp.end())