from conta_corrente import *

class Main:
  
    # cc1 = conta_corrente.Conta_Corrente(1234, 'Fulano', 100)
    numero = input('Digite o número da conta: ')
    nome = input('Digite o nome do correntista: ')
    saldo = float(input('Digite o saldo inicial: '))
    cc1 = Conta_Corrente(numero, nome, saldo)

    cc1.sacar(float(input('Digite o valor à sacar: R$')))
    cc1.depositar(float(input('Digite o valor à sacar: R$')))
    
    print('*' * 14)

    # cc2 = Conta_Corrente(5678, 'Ciclano', 200)
    numero = input('Digite o número da conta: ')
    nome = input('Digite o nome do correntista: ')
    saldo = float(input('Digite o saldo inicial: '))
    cc2 = Conta_Corrente(numero, nome, saldo)
    print('*' * 14)

    print('Dados da cc1...')
    print('Nome do correntista: '.format(cc1.nome_titular))
    print('Número da conta: '.format(cc1.numero_conta))
    print('Saldo: '.format(cc1.saldo))

    print('Dados da cc2...')
    print('Nome do correntista: {}'.format(cc2.nome_titular))
    print('Número da conta: {}'.format(cc2.numero_conta))
    print('Saldo: {}'.format(cc2.saldo))