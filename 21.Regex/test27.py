import re
s1 = 'hello abc 123 abc'
print('source:',s1)
m1 = re.search('abc',s1) #first occurence of abc from left to right.
print(m1)