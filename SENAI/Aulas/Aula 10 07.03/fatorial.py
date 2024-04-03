print('-' * 15)
print('Fatorial')
print('-' * 15)

num = int(input('\nNúmero: '))

for i in range(num, 0, -1):
    if i != 1:
        print('{} x '.format(i), end='')
    else:
        print('{} =  '.format(i), end='')