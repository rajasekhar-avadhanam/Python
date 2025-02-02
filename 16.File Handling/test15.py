try:
	f1 = open('give path to test2.txt','r')
	print(f1.read())
except BaseException as ex:
	print(ex)
finally:
	f1.close()

print('done')