import math
# Entrada
massaCorporea = float(input('Massa corpórea (kg): '))
altura = float(input('Altura (m): '))

# Processamento
imc = massaCorporea / math.pow(altura, 2) 

if imc < 16:
    # Saída
    print('IMC: {}\nMagreza grave')

elif (imc >= 16) and (imc < 17):
    # Saída
    print('IMC: {}\nMagreza moderada')

elif (imc >= 17) and (imc < 18.5):
    # Saída
    print('IMC: {}\nMagreza leve')

elif (imc >= 18.5) and (imc < 25):
    # Saída
    print('IMC: {}\nSaudável')

elif (imc >= 25) and (imc < 30):
    # Saída
    print('IMC: {}\nSobrepeso')

elif (imc >= 30) and (imc < 35):
    # Saída
    print('IMC: {}\nObesidade Grau I')

elif (imc >= 35) and (imc < 40):
    # Saída
    print('IMC: {}\nObesidade Grau II (severa)')

elif imc >= 40:
    # Saída
    print('IMC: {}\nObesidade Grau I (mórbida)')

