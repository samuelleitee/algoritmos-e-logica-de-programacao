# def numberAnalysis(numero):
#     if numero % 2 == 0 and numero > 0:
#         print('O número {} é par e positivo.'.format(numero))
#     elif numero % 2 == 0 and numero < 0:
#         print('O número {} é par e negativo.'.format(numero))
#     elif numero % 2 != 0 and numero > 0:
#         print('O número {} é ímpar e positivo.'.format(numero))
#     elif numero % 2 != 0 and numero > 0:
#         print('O número {} é ímpar e negativo.'.format(numero))
#     else: 
#         print('O número é nulo.')

def paridade():
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
    
def positivoOuNegativo():
    if numero > 0:
        return 'positivo'
    elif numero < 0:
        return 'negativo'
    else:
        return 'nulo'

try:
    numero = int(input('Digite um número inteiro: '))
except (ValueError):
    print('Valor inválido, tente novamente.')

print('O número {} é {} e {}.'.format(numero, paridade(), positivoOuNegativo()))