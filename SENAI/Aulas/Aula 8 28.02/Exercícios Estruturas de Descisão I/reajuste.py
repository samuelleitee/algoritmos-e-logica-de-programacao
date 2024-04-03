# Entrada
salario = float(input('Digite o salário do funcionário: R$'))

# Processamento
if salario <= 1000.00:
    aumento = salario * (20 / 100)
    novoSalario = salario + (salario * (20 / 100))

    # Saída
    print(f'\nSalário atual: R${salario :.2f}\nAumento: 20%\nValor do aumento: R${aumento :.2f}\nNovo salário: R${novoSalario :.2f} ')

elif salario <= 1700.00 and salario > 1000:
    aumento = salario * (15 / 100)
    novoSalario = salario + (salario * (15 / 100))

    # Saída
    print(f'\nSalário atual: R${salario :.2f}\nAumento: 15%\nValor do aumento: R${aumento :.2f}\nNovo salário: R${novoSalario :.2f} ')

elif salario <= 2300.00 and salario > 1700:
    aumento = salario * (10 / 100)
    novoSalario = salario + (salario * (10 / 100))

    # Saída
    print(f'\nSalário atual: R${salario :.2f}\nAumento: 10%\nValor do aumento: R${aumento :.2f}\nNovo salário: R${novoSalario :.2f} ')

elif salario > 2300.00:
    aumento = salario * (5 / 100)
    novoSalario = salario + (salario * (5 / 100))

    # Saída
    print(f'\nSalário atual: R${salario :.2f}\nAumento: 5%\nValor do aumento: R${aumento :.2f}\nNovo salário: R${novoSalario :.2f} ')