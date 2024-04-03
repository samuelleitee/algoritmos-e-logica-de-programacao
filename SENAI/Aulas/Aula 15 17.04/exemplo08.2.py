numeros = []
quantos_numeros = int(input('Quantos números você deseja incluir na lista: '))

for i in range(quantos_numeros):
    numero = int(input(f'Digite o {i+1}º número inteiro: '))
    numeros.append(numero)

print(numeros)