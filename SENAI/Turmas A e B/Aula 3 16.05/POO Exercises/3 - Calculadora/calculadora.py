class Calculadora:
  def __init__(self, numero1, numero2):
    self.numero1 = numero1
    self.numero2 = numero2

  def somar(self):
    soma = self.numero1 + self.numero2
    print('{} + {} = {}'.format(self.numero1, self.numero2, soma))

  def subtrair(self):
    subtracao = self.numero1 - self.numero2
    print('{} - {} = {}'.format(self.numero1, self.numero2, subtracao))

  def multiplicar(self):
    multiplicacao = self.numero1 * self.numero2
    print('{} * {} = {}'.format(self.numero1, self.numero2, multiplicacao))

  def dividir(self):
    divisao = self.numero1 / self.numero2
    print('{} / {} = {}'.format(self.numero1, self.numero2, divisao))

aux = False
while not aux:
  try: 
    numero1 = int(input('Digite o primeiro número: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

aux = False
while not aux:
  try: 
    numero2 = int(input('Digite o segundo número: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

calculadora = Calculadora(numero1, numero2)

print('[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão\n')

aux = False
while not aux:
  try: 
    operacao = int(input('Escolha uma operação: '))
    aux = True
  except (ValueError):
    print('Opção inválida, tente novamente.')

if operacao == 1:
  calculadora.somar()
elif operacao == 2:
  calculadora.subtrair()
elif operacao == 3:
  calculadora.multiplicar()
elif operacao == 4:
  calculadora.dividir()