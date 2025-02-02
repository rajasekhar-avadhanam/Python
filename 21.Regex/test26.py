import re
s1 = 'a1aabcaaa234aaaahelloaaaaatest'
print('source:',s1)
m1 = re.finditer('a{,3}',s1) #{,3} from 0 to 3 a's
for exp in m1:
	print('search str',exp.group(),'start',exp.start(),'end:',exp.end())