# Entrada
consumo = float(input('Consumo (m³): '))

# Processamento
if consumo <= 10:
    valor = 22.38

    # Saída
    print('Conta: R${:.2f}'.format(valor))
    
# Processamento
if consumo <= 20:
    valor = consumo * 3.50

    # Saída
    print('Conta: R${:.2f}'.format(valor))

# Processamento
if consumo <= 50:
    valor = consumo * 8+75

    # Saída
    print('Conta: R${:.2f}'.format(valor))

# Processamento
else:
    valor = consumo * 9.64

    # Saída
    print('Conta: R${:.2f}'.format(valor))
