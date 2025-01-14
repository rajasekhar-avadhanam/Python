# logical

x = 10
y = 10
z = 20
print('x ==10 and y = 10 : ', (x ==10 and y == 10))
print('x ==10 and y = 20 : ', (x ==10 and y == 20))
print('x ==10 or y = 20 : ', (x ==10 or y == 20))
print('x ==10 or y = 10 : ', (x ==10 or y == 10))
print('not (x ==10): ', not (x==10))
print('not (x ==10 and y == 10): ', not (x==10 and y == 10))
print('not (x ==10 and z == 10): ', not (x==10 and z == 10))
print('not (x ==10 or y == 10): ', not (x==10 or z == 30))
print('not (z ==10): ', not(z == 10))
print('not (z ==20): ', not(z == 20))
