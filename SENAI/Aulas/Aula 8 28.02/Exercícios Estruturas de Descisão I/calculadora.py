# Entrada
print('-' * 10)
print('1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Potência\n6 - Raiz quadrada\n7 - Número par\n8 - Número ímpar')
print('-' * 10)

calculo = int(input('Escolha uma operação: '))

# Processamento
if calculo == 1:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    resultado = num1 + num2
    
    # Saída
    print('{} + {} = {:.2f}'.format(num1, num2, resultado))

elif calculo == 2:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    resultado = num1 - num2
    
    # Saída
    print('{} - {} = {:.2f}'.format(num1, num2, resultado))

elif calculo == 3:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    resultado = num1 * num2
    
    # Saída
    print('{} * {} = {:.2f}'.format(num1, num2, resultado))

elif calculo == 4:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    resultado = num1 / num2
    
    # Saída
    print('{} / {} = {:.2f}'.format(num1, num2, resultado))

elif calculo == 5:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    
    resultado = num1 ** num2
    
    # Saída
    print('{} ** {} = {:.2f}'.format(num1, num2, resultado))

elif calculo == 6:

    num1 = int(input('Digite um número: '))
    
    resultado = num1 ** (1 / 2)
    
    # Saída
    print(f'{num1} ** (1 / 2) = {resultado :.2f})')

elif calculo == 7:

    num1 = int(input('Digite um número: '))
    
    resultado = num1 % 2
    
    # Saída
    if resultado == 0:
        print('O número é par.')
    else:
        print('O número não é par.')

elif calculo == 8:

    num1 = int(input('Digite um número: '))
    
    resultado = num1 % 2
    
    # Saída
    if resultado == 0:
        print('O número não é ímpar.')
    else:
        print('O número é ímpar.')