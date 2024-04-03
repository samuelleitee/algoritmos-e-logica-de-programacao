# Crie um programa que leia/solicite para o usuário inserir dois números, realize a multiplicação entre eles e mostre na tela o resultado.

# Entrada
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

# Processamento
multiplicacao = numero1 * numero2

# Saída
print('{:.2f} x {:.2f} = {:.2f}'.format(numero1, numero2, multiplicacao))