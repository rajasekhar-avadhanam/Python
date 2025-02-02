f1 = open('hello4.txt','x') #exclusive mode---if file available gives error, if itsnt available it runs
f1.write('new file always')
f1.close()