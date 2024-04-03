my_list = [1, 2, 3, 4, 5]
listaPares = []
listaImpares = []

print('Lista: ', end='' )
print(*my_list, sep=', ')
print(f'Maior: {max(my_list)}')
print(f'Menor: {min(my_list)}')

for i in my_list:
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)    

print('Pares: ', end='')
print(*listaPares, sep=', ')
print('Ímpares: ', end='')
print(*listaImpares, sep=', ')