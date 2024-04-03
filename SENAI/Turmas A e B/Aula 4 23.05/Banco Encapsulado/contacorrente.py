class ContaCorrente:
    def __init__(self, numero_conta, cliente, saldo):
        self.__numero_conta = numero_conta
        self.__cliente = cliente
        self.__saldo = saldo   
    
    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente')

        else:
            self.__saldo -= valor
            print(f'Saque realizado com sucesso!\nSaldo: {self.__saldo}')

    def depositar(self, valor):
        self.__saldo += valor
        print(f'Deposito realizado com sucesso!\nSaldo: {self.__saldo}')

    def extrato(self):
        print(f'Número da conta: {self.__numero_conta}')
        self.__cliente.exibir_dados()
        print(f'Saldo: {self.__saldo}')