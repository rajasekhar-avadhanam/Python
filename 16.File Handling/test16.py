try:
	f1 = open('give path to 1.jpg','rb') #rb--read in binary
	f2 = open('hello4.jpg','wb') #wb-- write in binary
	b1 = f1.read()
	f2.write(b1)
except BaseException as err:
	print(err)
finally:
	f1.close()
	f2.close()

print('done')