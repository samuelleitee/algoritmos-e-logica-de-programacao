a = int(input('Type a number: '))
b = int(input('Type another number: '))

if a > b:
    print('The difference between the greatest and the number is {}.'.format(a-b))
elif b > a:
    print('The difference between the greatest and the number is {}.'.format(b-a))
else:
    print('The numbers are equal and the difference between them is zero.')
