from array import *

matriz = [
    [0, 0, 0], 
    [0, 0, 0], 
    [0, 0, 0]
]

for i in range(0, 3):
    for j in range(0, 3):

        aux = False
        while not aux:
                
            print('Digite o elemento a[{}][{}]: '.format(i, j), end='')

            try:
                matriz[i][j] = int(input())
                aux = True
            except (ValueError):
                print('Valor inválido, digite um número inteiro.')

print('\nMatriz:\n')
print(*matriz, sep='\n')