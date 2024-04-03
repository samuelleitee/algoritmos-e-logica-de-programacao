# Entrada
consumo = float(input('Consumo (m³): '))

# Processamento
if consumo <= 10:
    valor = 44.95

    # Saída
    print('Conta: R${:.2f}'.format(valor))
    
# Processamento
if consumo <= 20:
    valor = consumo * 8.75

    # Saída
    print('Conta: R${:.2f}'.format(valor))
    
# Processamento
if consumo <= 50:
    valor = consumo * 16.76

    # Saída
    print('Conta: R${:.2f}'.format(valor))
    
# Processamento
else:
    valor = consumo * 17.46

    # Saída
    print('Conta: R${:.2f}'.format(valor))
    