try:
	f1 = open('give path to test2.txt','a')
	f1.write('abc')
	f1.write('abc')
	f1.write('abc')
except BaseException as ex:
	print(ex)
finally:
	f1.close() # need to close connection because a lot of resirces may be used for this open connection

print('done')