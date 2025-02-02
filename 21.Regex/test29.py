import re
s1 = "hello abc and how is xyz amd what about the test in the year 500?"
print(s1)
r1 = re.findall('abc',s1)
print(r1)
for item in r1:
	print(item)