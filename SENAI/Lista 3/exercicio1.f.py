counter = 0
lista = []

while counter < 200:
    if counter % 4 == 0:
        lista.append(counter)
    counter += 1

print('Valores divisíveis por 4 e menores que 200: ', end='')
print(*lista, sep=', ', end='.')