import math

x = int(input('Insert Point X: '))
y = int(input('Insert Point Y: '))
r = int(input('Insert Point R: '))

hypotenuse = math.sqrt(pow(x, 2) + pow(y, 2))

if hypotenuse <= r:
    print('The points belongs to Circle')
else:
    print('The point does not belongs to circle')
