cont = 1
while cont <= 9:
    num = int(input('Digite o {}º número: '.format(cont + 1)))
    print('{}º número digitado é: {}'.format(cont + 1, num))
    cont += 1