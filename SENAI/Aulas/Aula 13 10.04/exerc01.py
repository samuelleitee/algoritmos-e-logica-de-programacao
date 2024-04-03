import math

def potenciacao(base, exp):
    if base > 0:
        print(f'{base} ** {exp} = {math.pow(base, exp) :.0f}')
    elif base < 0:
        print(f'({base}) ** {exp} = {math.pow(base, exp) :.0f}')
    elif base == 0 and exp == 0:
        print(f'{base} ** {exp} == indeterminado')

print('-' * 11 + 'Potenciação' + '-' * 11 + '\n')

aux = False

while not aux:
    try:
        x = int(input('Base: '))
        aux = True
    except (ValueError):
        print('Valor inválido, tente novamente.')

aux = False

while not aux:
    try:
        y = int(input('Expoente: '))
        aux = True
    except (ValueError):
        print('Valor inválido, tente novamente.')

potenciacao(x, y)