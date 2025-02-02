import re
s1 = "hello abc and how is abc amd what about the abc in the year 500?"
words = re.split('\s',s1)
for word in words:
	print(word)