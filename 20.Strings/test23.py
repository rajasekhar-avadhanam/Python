default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n---Default Order----')
print(default_order)

positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n---Positional Order---')
print(positional_order)


keyword_order = "{s}, {b} and {j}".format(j = 'John',b = 'Bill',s = 'Sean')
print('\n---Keyword order---')
print(keyword_order)