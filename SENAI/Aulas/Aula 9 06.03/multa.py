velocidade = int(input('Digite a velocidade (km/h): '))
print('\nLimite: 80km/h')

if velocidade > 80:
    print('Você foi multado.')

    excesso = velocidade - 80
    multa = 50 * excesso
    print('Valor da multa: R${:.2f}'.format(multa))