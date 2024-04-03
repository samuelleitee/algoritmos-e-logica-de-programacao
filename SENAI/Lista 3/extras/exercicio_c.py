pares = []
impares = []

for i in range(20):
    aux = False
    
    while not aux:
        try:
            numero = int(input('Digite o {}º número inteiro: '.format(i + 1)))

            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)

            aux = True

        except (ValueError):
            print('Valor inválido, tente novamente.')

print('{} números são pares: '.format(len(pares)), end='')
print(*pares, sep=', ', end='.')
print('{} números são ímpares: '.format(len(impares)), end='')
print(*impares, sep=', ', end='.')