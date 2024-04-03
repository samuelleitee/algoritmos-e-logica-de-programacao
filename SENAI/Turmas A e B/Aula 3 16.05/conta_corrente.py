class Conta_Corrente:
    def __init__(self, numero_conta, nome_titular, saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo insuficiente.')
        else:
            self.saldo -= valor
            print('Saldo após saque: R${:.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        print('Depósito efetuado')

    def imprimir_extrato(self):
        print('Nome do correntista: '.format(self.nome_titular))
        print('Número da conta: '.format(self.numero_conta))
        print('Saldo: '.format(self.saldo))
        # print('Extrato = R${:.2f}'.format(self.saldo))