from array import array

matrizA = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
matrizB = []

for element in matrizA:
    if element % 2 == 0:
        element *= 3
        matrizB.append(element)
    else:
        element *= 2
        matrizB.append(element)

print('Matriz A: ', end='')
print(*matrizA, sep=', ', end='.\n')
print('Matriz B: ', end='')
print(*matrizB, sep=', ', end='.')