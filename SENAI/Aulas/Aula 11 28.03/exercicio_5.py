lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
nonRepeatedLista = []

for i in lista:
    if i not in nonRepeatedLista:
        nonRepeatedLista.append(i)

print('Lista: ', end='')
print(*lista, sep=', ')
print('Lista sem repetições: ', end='')
print(*nonRepeatedLista, sep=', ')