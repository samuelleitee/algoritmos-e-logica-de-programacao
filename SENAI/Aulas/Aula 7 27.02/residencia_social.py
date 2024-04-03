# Entrada
consumo = float(input('Consumo (m³): '))

# Processamento
if consumo <= 3:
    valor = 7.59

    # Saída
    print('Conta: R${:.2f}'.format(valor))

if consumo <= 20:
    valor = consumo  * 1.31

    # Saída
    print('Conta: R${:.2f}'.format(valor))

if consumo <= 30:
    valor = consumo  * 4.64

    # Saída
    print('Conta: R${:.2f}'.format(valor))

if consumo <= 50:
    valor = consumo  * 6.62

    # Saída
    print('Conta: R${:.2f}'.format(valor))

else:
    valor = consumo  * 7.31

    # Saída
    print('Conta: R${:.2f}'.format(valor))