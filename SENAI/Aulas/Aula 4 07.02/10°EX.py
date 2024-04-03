# Crie um programa que leia/solicite para o usuário inserir quatro notas, realize a média e mostre na tela o resultado.

# Entrada
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))

# Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída
print('A média final é {:.2f}.'.format(media))
