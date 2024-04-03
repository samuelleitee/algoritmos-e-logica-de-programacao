from cliente import Cliente
from contacorrente import ContaCorrente

cliente1 = Cliente('Fulano', 1234)
cliente2 = Cliente('Beltrano', 5678)

cc1 = ContaCorrente(1, cliente1, 100)
cc2 = ContaCorrente(2, cliente2, 200)

print('Dados do cliente 1')
cliente1.exibir_dados()
print(f'\nDados da conta corrente 1')
cc1.extrato()

print('*' * 12)

print('\nDados do cliente 2')
cliente2.exibir_dados()
print(f'\nDados da conta corrente 2')
cc2.extrato()

print(cc1)