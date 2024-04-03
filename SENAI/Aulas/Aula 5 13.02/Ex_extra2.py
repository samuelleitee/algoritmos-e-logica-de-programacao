a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))

aux = a
a = b
b = aux

print('a: {}\nb: {}'.format(a, b))