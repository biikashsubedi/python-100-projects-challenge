x = float(input('Insert coordinate of point x: '))
y = float(input('Insert coordinate of point y: '))

if x > 0 and y > 0:
    print('This is first quadrant')
elif x < 0 and y > 0:
    print('This is second quadrant')
elif x > 0 and y < 0:
    print('this is third quadrant')
elif x < 0 and y < 0:
    print('this is forth quadrant')
elif x == 0:
    print('this is X quadrant')
elif y == 0:
    print('this is Y quadrant')
