print('Números ímpares entre 0 e 20: ', end='')
impares = []

for numero in range(21):
    if numero % 2 != 0:
        impares.append(numero) 

print(*impares, sep=', ', end='.')