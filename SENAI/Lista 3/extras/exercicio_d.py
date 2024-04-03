lista = []

for i in range(10):
    aux = False
    
    while not aux:
        try:
            numero = int(input('Digite o {}º número inteiro: '.format(i + 1)))
            lista.append(numero)
            aux = True
        except (ValueError):
            print('Valor inválido, tente novamente.')

print('\nNúmeros: ', end='')
print(*lista, sep=', ', end='.\n')
print('Maior: {}'.format(max(lista)))
print('Menor: {}'.format(min(lista)))
print('Soma: {}'.format(sum(lista)))
print('Média: {}'.format(sum(lista) / len(lista)))