import re

m1 = re.finditer('[ab]','abc123aabcxyzabchelloabc') #[ab] serahces for a and b individually.
for exp in m1:
	print('search str:',exp.group(),'start:',exp.start(),'end:',exp.end())