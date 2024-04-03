from array import *

matrizA = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
matrizB = array('i', [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])

matrizC = matrizA + matrizB

print('Matriz A: [', end='')
print(*matrizA, sep=', ', end=']\n\n')

print('Matriz B: [', end='')
print(*matrizB, sep=', ', end=']\n\n')

print('Matriz C (A + B): [', end='')
print(*matrizC, sep=', ', end=']')