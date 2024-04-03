cont = 1
numeros = []

while cont <= 50:
    numeros.insert(cont - 1, cont)
    cont += 1

for i in numeros:
    if i < 50:
        print('{} + '.format(i), end='')
    else:
        print('{} = {}'.format(i, sum(numeros)))