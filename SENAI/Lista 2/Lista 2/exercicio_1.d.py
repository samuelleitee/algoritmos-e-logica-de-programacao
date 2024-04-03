import os
import time

print('-' * 25)
print('Equação de segundo grau\n      ax² + bx + c') 
print('-' * 25)

auxA = False
auxB = False
auxC = False

while not auxA:
    try:
        a = float(input('Informe o valor de a: '))
        auxA = True
    except (ValueError):
        print('Valor inválido. Digite apenas números.')   
        time.sleep(1)
        os.system('cls') 

while not auxB:
    try:
        b = float(input('Informe o valor de b: '))
        auxB = True
    except (ValueError):
        print('Valor inválido. Digite apenas números.')   
        time.sleep(1)
        os.system('cls') 

while not auxC:
    try:
        c = float(input('Informe o valor de c: '))
        auxC = True
    except (ValueError):
        print('Valor inválido. Digite apenas números.')   
        time.sleep(1)
        os.system('cls') 

os.system('cls')

print('-' * 25)
print('Equação de segundo grau\n      ax² + bx + c') 
print('-' * 25)
print('A: {:.2f}\nB: {:.2f}\nC: {:.2f}'.format(a, b, c))

delta = (b ** 2) - (4 * a * c)
x1 = (-b + delta ** (1 / 2)) / 2 * a
x2 = (-b - delta ** (1 / 2)) / 2 * a

if delta < 0:
    print('Não há raízes reais.')

elif delta > 0:
    print('\nHá duas raízes reais distintas.\n S = {' + str(x1) + ', ' + str(x2) + '}')

else:
    print('\nHá duas raízes reais iguais.\n S = {' + str(x1) + ', ' + str(x2) + '}')