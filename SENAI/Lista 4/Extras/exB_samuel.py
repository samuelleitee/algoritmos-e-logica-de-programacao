matrizA = []

aux = False
while not aux:
    try:
        number = int(input('Escolha um número para descobrir a tabuada [1 - 10]: '))
        if number > 0 and number <= 10:
            aux = True
        else:
            print('Número inválido, tente novamente.')
    except (ValueError):
        print('Valor inválido, tente novamente.')

for i in range(10):
    # print('%d x %d = %d' % (number, i + 1, number * (i + 1)))
    print('{} x {} = {}'.format(number, i + 1, number * (i + 1)))
    multTable = number * (i + 1)
    matrizA.append(multTable)

print('Matriz A (Tabuada do {}): '.format(number), end='')
print(*matrizA, sep=', ', end='.')