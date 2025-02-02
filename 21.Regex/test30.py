import re
s1 = "hello abc and how is abc amd what about the abc in the year 500?"
print(s1)
r1 = re.match('hello',s1) # used to compare the start chars of string
print(r1)
r2 = re.match('abc',s1)
print(r2)
