class IANESBank:
  def __init__(self, nome_titular, numero_conta, saldo):
    self.nome_titular = nome_titular
    self.numero_conta = numero_conta
    self.saldo = saldo

  def sacar(self):
    aux = False
    while not aux:
      try:
        valor = float(input('Digite o valor à sacar: R$'))
        if valor > 0:
          aux = True
        else: 
          print('Valor inválido, tente novamente.')
      except (ValueError):
        print('Valor inválido, tente novamente.')

    if valor > self.saldo:
      print('Saldo insuficiente!\n')
      opcoes_conta()
    else:
      self.saldo -= valor
      print(f'\nValor sacado: R${valor:.2f}')
      print(f'Saldo após saque: R${self.saldo:.2f}\n')
      opcoes_conta()

  def depositar(self):
    aux = False
    while not aux:
      try:
        valor = float(input('Digite o valor à depositar: R$'))
        if valor > 0:
          aux = True
        else: 
          print('Valor inválido, tente novamente.')
      except (ValueError):
        print('Valor inválido, tente novamente.')
    
    self.saldo += valor
    print(f'\nValor depositado: R${valor:.2f}')
    print(f'Saldo após o depósito: R${self.saldo:.2f}\n')
    opcoes_conta()

  def imprimir_extrato(self):
    print(f'\n\n*****Extrato*****\n\nNome do titular: {conta.nome_titular}\nNúmero da conta: {conta.numero_conta}\nSaldo: R${conta.saldo:.2f}\n*****************\n')
    opcoes_conta()
 
usuarios = []
senhas = []

def opcoes_iniciais():
  print('[1] Entrar\n[2] Criar conta\n[3] Sair')

  aux = False
  while not aux:
    try: 
      opcao = int(input('\nEscolha uma opção: '))
      aux = True
    except (ValueError):
      print('Opção inválida, tente novamente.')

  if opcao == 1:
    usuario = input('Nome do titular: ')
    senha = input('Senha: ')

    if usuario in usuarios and senha in senhas:
      for i in usuarios:
        if usuario == i:
          if senha == senhas[usuarios.index(i)]:
            print('\nLogin efetuado com sucesso!\n')
            opcoes_conta()
    else: 
      print('\nLogin e/ou senhas inválidos. Tente novamente ou crie uma conta.\n')
      opcoes_iniciais()

  if opcao == 2:
    usuario = input('Digite o nome do titular: ')
    senha = input('Digite uma senha forte: ')

    aux = False
    while not aux:
      try: 
        saldo = float(input('Insira um valor inicial à conta: R$'))
        if saldo < 0:
          print('Valor inválido, tente novamente.')
        else:
          aux = True
      except (ValueError):
        print('Valor inválido, tente novamente.')

    aux = False
    while not aux:
      try: 
        numero_conta = int(input('Escolha um número de 5 dígitos para a sua conta: '))
        if numero_conta < 10000 or numero_conta > 99999:
          print('Valor inválido, tente novamente.')
        else:
          aux = True
      except (ValueError):
        print('Valor inválido, tente novamente.')

    usuarios.append(usuario)
    senhas.append(senha)

    global conta
    conta = IANESBank(usuario, numero_conta, saldo)

    print('Conta criada com sucesso!\n')
    opcoes_iniciais()

  if opcao == 3:
    print('Goodbye!')

def opcoes_conta():
  print('[1] Sacar\n[2] Depositar\n[3] Imprimir extrato\n[4] Sair')

  aux = False
  while not aux:
    try: 
      opcao = int(input('\nEscolha uma opção: '))
      aux = True
    except (ValueError):
      print('Opção inválida, tente novamente.')

  if opcao == 1:
    conta.sacar()
  if opcao == 2:
    conta.depositar()
  if opcao == 3:
    conta.imprimir_extrato()
  if opcao == 4:
    opcoes_iniciais()
  
opcoes_iniciais()