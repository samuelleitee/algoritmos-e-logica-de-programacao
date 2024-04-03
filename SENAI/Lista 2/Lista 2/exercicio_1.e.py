countA = False
countB = False
countC = False
lista = []

while not countA:

    try:
        a = int(input('Digite o 1º número inteiro: '))
        lista.append(a)
        countA = True

    except (ValueError):
        print('Valor inválido. Digite apenas valores numéricos e inteiros.')

while not countB:

    try:
        b = int(input('Digite o 2º número inteiro: '))
        lista.append(b)
        countB = True

    except (ValueError):
        print('Valor inválido. Digite apenas valores numéricos e inteiros.')

while not countC:

    try:
        c = int(input('Digite o 3º número inteiro: '))
        lista.append(c)
        countC = True

    except (ValueError):
        print('Valor inválido. Digite apenas valores numéricos e inteiros.')

maior = max(lista)
menor = min(lista)
lista.remove(max(lista))
lista.remove(min(lista))

print('Ordem crescente: {}, {}, {}.'.format(menor, lista[0], maior))