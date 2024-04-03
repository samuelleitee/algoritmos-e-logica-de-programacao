minha_lista5 = [1, 3, 2, 5, 4]

minha_lista5.sort()
print('Crescente: ', end='')
print(*minha_lista5, sep=', ')

print('Decrescente: ', end='')
print(*sorted(minha_lista5, reverse=True), sep=', ')