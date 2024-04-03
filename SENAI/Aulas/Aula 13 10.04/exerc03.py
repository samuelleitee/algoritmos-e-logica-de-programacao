def indiceDeMassaCorporea(peso, altura):
    imc = peso / altura ** 2
    print('IMC: {:.2f} Kg/m²'.format(imc))

aux = False

while not aux:
    try:
        peso = float(input('Peso (Kg): '))
        aux = True
    except (ValueError):
        print('Valor inválido, tente novamente')

aux = False

while not aux:
    try:
        altura = float(input('Altura (m): '))
        aux = True
    except (ValueError):
        print('Valor inválido, tente novamente')

indiceDeMassaCorporea(peso, altura)