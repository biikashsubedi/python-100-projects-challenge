mdv = input('Choose one to calculate (M, D & V): ')

if mdv == 'm':
    d = float(input('Input Density: '))
    v = float(input('Input Volume: '))
    # this is mass formula
    result = d*v
elif mdv == 'd':
    m = float(input('Input Float: '))
    v = float(input('Input Float: '))
    # this is density formula
    result = m/v
elif mdv == 'v':
    m = float(input('Input Mass: '))
    d = float(input('Input Density: '))
    # this is volume formula
    result = m/d

print('%.2f' % result)