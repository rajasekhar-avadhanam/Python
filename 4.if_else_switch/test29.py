def switchDef(caseValue):
	def monday():
		print('i am from monday')
	def tuesday():
		print('i am from tuesday')
	def wednesday():
		print('i am from wednesday')
	def thursday():
		print('i am from thursday')
	def friday():
		print('i am from friday')
	def satuarday():
		print('i am from satuarday')
	def sunday():
		print('i am from sunday')
	weekDictionary={
	    1: monday,
	    2: tuesday,
	    3: wednesday,
	    4: thursday,
	    5: friday,
	    6: satuarday,
	    7: sunday,
	}

	weekDictionary.get(caseValue)()

switchDef(1)
print('--------')
switchDef(3)
print('--------')
switchDef(5)
print('--------')
switchDef(7)
print('--------')

