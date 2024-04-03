from array import *

matrizA = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
matrizB = array('i', [])

for element in matrizA:
    element = element * 3
    matrizB.append(int(element))

print('Matriz A: [', end='')
print(*matrizA, sep=', ', end=']\n\n')

print('Matriz B (A * 3): [', end='')
print(*matrizB, sep=', ', end=']')