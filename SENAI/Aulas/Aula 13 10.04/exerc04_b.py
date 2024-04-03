from exerc04 import *
lista = [] 
aux = False
while not aux:
    try:
        n = int(input('Número de elementos a incluir na lista: '))
        if n > 0:
            aux = True
        else:
            print('Valor inválido, tente novamente.')
    except (ValueError):
        print('Valor inválido, tente novamente.')

for i in range(1, n + 1):
    aux = False
    while not aux:
        print('Digite o {}º número inteiro: '.format(i), end='')
        try:
            i = int(input(''))
            lista.append(i)
            aux = True 
        except (ValueError):
            print('Valor inválido, tente novamente.')

print('\nLista: ', end='')
print(*lista, sep=', ', end='.\n\n')

maiorLista(lista)
menorLista(lista)
somaLista(lista)
mediaLista(lista)