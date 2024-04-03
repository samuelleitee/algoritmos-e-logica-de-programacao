execucao = False
while execucao == False:
    num = int(input('Tabuada do número: '))
    count = 1

    while count < 11:
        print('{} X {} = {}'.format(num, count, num * count))
        count += 1

    continuacao = input('Você deseja continuar [S/N]? ').upper()

    if continuacao == 'S':
        execucao = False
    else:
        print('Até a próxima!!!')
        execucao = True