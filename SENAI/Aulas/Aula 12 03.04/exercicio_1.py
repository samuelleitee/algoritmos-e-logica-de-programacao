minha_lista1 = []

for i in range(0, 10):
    minha_lista1.append(i)

print('Lista: ', end='')
print(*minha_lista1, sep=', ')