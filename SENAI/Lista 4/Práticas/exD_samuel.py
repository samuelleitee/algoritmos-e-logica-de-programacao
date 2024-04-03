from array import *
from math import pow

matrizA = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
matrizB = array('i', [])

for element in matrizA:
    element = pow(element, 2)
    matrizB.append(int(element))

print('Matriz A: [', end='')
print(*matrizA, sep=', ', end=']\n\n')

print('Matriz B (QUADRADO ²): [', end='')
print(*matrizB, sep=', ', end=']')