salario = float(input('Salário: R$'))

# Desconto INSS
if salario <= 1302.00:
    inss = salario * (7.5 / 100)
    salarioDescInss = salario - inss
    print('\nSalário Inicial: {:.2f}'. format(salario))
    print('Desconto INSS (7.5%): {:.2f}'.format(inss))

elif salario >= 1302.01 and salario <= 2571.29:
    inss = salario * (9 / 100)
    salarioDescInss = salario - inss
    print('\nSalário Inicial: {:.2f}'. format(salario))
    print('Desconto INSS (9%): {:.2f}'.format(inss))

elif salario >= 2571.30 and salario <= 3856.94:
    inss = salario * (12 / 100)
    salarioDescInss = salario - inss
    print('\nSalário Inicial: {:.2f}'. format(salario))
    print('Desconto INSS (12%): {:.2f}'.format(inss))

elif salario >= 3856.95 and salario <= 7507.49:
    inss = salario * (14 / 100)
    salarioDescInss = salario - inss
    print('\nSalário Inicial: {:.2f}'. format(salario))
    print('Desconto INSS (14%): {:.2f}'.format(inss))

# Desconto IRRF
if salarioDescInss <= 1903.98:  
    salarioFinal = salarioDescInss
    print('Desconto IRRF (0%): {:.2f}'.format(irrf))
    print('Salário com os descontos: {:.2f}'.format(salarioFinal))

elif salarioDescInss >= 1903.99 and salarioDescInss <= 2826.65:
    irrf = salarioDescInss * (7.5 / 100)
    salarioFinal = salarioDescInss - irrf
    print('Desconto IRRF (7.5%): {:.2f}'.format(irrf))
    print('Salário com os descontos: {:.2f}'.format(salarioFinal))

elif salarioDescInss >= 2826.66 and salarioDescInss <= 3751.05:
    irrf = salarioDescInss * (15 / 100)
    salarioFinal = salarioDescInss - irrf
    print('Desconto IRRF (15%): {:.2f}'.format(irrf))
    print('Salário com os descontos: {:.2f}'.format(salarioFinal))

elif salarioDescInss >= 3751.06 and salarioDescInss <= 4664.68:
    irrf = salarioDescInss * (22.5 / 100)
    salarioFinal = salarioDescInss - irrf
    print('Desconto IRRF (22.5%): {:.2f}'.format(irrf))
    print('Salário com os descontos: {:.2f}'.format(salarioFinal))

elif salarioDescInss >= 4664.68:
    irrf = salarioDescInss * (27.5 / 100)
    salarioFinal = salarioDescInss - irrf
    print('Desconto IRRF (27.5%): {:.2f}'.format(irrf))
    print('Salário com os descontos: {:.2f}'.format(salarioFinal))
