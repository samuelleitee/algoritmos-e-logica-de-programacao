from math import factorial

matrizA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
matrizB = []

for element in matrizA:
    element = factorial(element)
    matrizB.append(element)

print('Matriz A: [', end='')
print(*matrizA, sep=', ', end=']\n\n')

print('Matriz B (FATORIAL !): [', end='')
print(*matrizB, sep=', ', end=']')