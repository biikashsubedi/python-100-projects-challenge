print('Insert Length of purposed Triangle: ')

x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))

if x+y>z and x+z>y and y+z>x:
    print('Yea! This is Triangle')
else:
    print('NO, NO this is not triangle!!!')