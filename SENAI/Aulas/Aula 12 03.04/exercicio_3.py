minha_lista3 = ['A', 'B', 'C']

print('Lista: ', end='')
print(*minha_lista3, sep=', ')

x = minha_lista3.pop()

print('Nova lista: ', end='')
print(*minha_lista3, sep=', ')
print('Elemento removido: {}'.format(x))