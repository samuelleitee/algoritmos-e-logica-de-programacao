aux = False
while not aux:
    try:
        auxiliary = int(input('Número que desejas saber a tabuada: '))  
        aux = True
    except (ValueError):
        print('Valor inválido, tente novamente')

print('-' * 40)

for i in range(11):
    print('{} x {} = {}'.format(auxiliary, i, auxiliary * i))