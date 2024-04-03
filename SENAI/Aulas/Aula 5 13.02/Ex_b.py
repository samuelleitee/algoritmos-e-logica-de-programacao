n = int(input('Type a number: '))

if n < 0:
    print('The positive values of {} is {}.'.format(n, n * -1))
else: 
    print('O número {} já é positivo.'.format(n))