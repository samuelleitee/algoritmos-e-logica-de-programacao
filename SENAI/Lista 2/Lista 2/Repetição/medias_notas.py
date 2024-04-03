import os
import time

aux = False
count = 1
lista = []
num = 0

while not aux:
    try:
        n = int(input('Número de notas a calcular (1-6): '))
        if n < 1 or n > 6: 
            print('Número inválido, tente novamente')
            time.sleep(1)
            os.system('cls')

        else:
            aux = True
    except (ValueError):
        print('Número inválido, tente novamente')
        time.sleep(1)
        os.system('cls')

while count <= n:
    try:
        print(f'Digite a {count}ª nota (1-10): ', end='')
        nota = float(input(''))
        if nota < 0 or nota > 10:
            print('Número inválido, tente novamente')
            time.sleep(1)
            os.system('cls')
        else:
            lista.append(nota)
            count += 1
    except (ValueError):
        print('Número inválido, tente novamente')
        time.sleep(1)
        os.system('cls')

for i in (lista):
    print('{}ª Nota: {}'.format(num + 1, lista[num]))
    num += 1

print('Média: {}'.format(sum(lista) / len(lista)))