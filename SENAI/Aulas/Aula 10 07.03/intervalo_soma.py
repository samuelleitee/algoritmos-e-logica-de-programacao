num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
lista = []

for i in range(num1, num2 + 1):
    lista.append(i)
    print(i, end=' ')

print('\nSoma: {}'.format(sum(lista)))