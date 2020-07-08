num = float(input("Enter number to check POSITIVE or NEGATIVE: "))

if num<0:
    print(f'{num} is NEGATIVE number')
elif num>0:
    print(f'{num} is POSITIVE number')
else:
    print('This is ZERO')