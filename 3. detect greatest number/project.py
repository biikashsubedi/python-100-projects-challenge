a = int(input('Enter First Number: '))
b = int(input('Enter Second Number: '))
c = int(input('Enter Third Number: '))

print('The maximum number is: ', end='')

if a <= b >=c:
    print(b)
elif b <= c >= a:
    print(c)
else:
    print(a)