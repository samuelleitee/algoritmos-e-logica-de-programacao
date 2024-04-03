lista = []
listaPar = []
listaImpar = [] 
count = 1

while count < 6:
    print('Digite o {}° número: '.format(count), end='')
    num = int(input(''))
    lista.append(num)

    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)

    count += 1

print('Maior: {}\nMenor: {}\nSoma: {}\nMédia: {}'.format(max(lista), min(lista), sum(lista), sum(lista) / 5))
print('Pares: ', end='')
print(*listaPar, sep=", ")
print('Ímpares: ', end='')
print(*listaImpar, sep=", ")