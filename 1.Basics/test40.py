
import keyword

print('abc'.isidentifier())
print('xyz'.isidentifier())
print('_test'.isidentifier())
print('t1'.isidentifier())
print('t#'.isidentifier())  #---> only _ is allowed
print('abc test'.isidentifier()) #---> sace is also a spl charcter which s not allowed
print('4t'.isidentifier())
print('True'.isidentifier())
print('If'.isidentifier())
print('Try'.isidentifier())
print('else'.isidentifier())


print(keyword.iskeyword('a'))
print(keyword.iskeyword('True'))

'''
in isidentifier() if we give a keyword even then
it will give the output as true because
it only check the rules for naming an identifier

'''