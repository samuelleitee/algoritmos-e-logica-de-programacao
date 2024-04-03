class Boletim:
  def __init__(self, nota1, nota2, nota3, nota4):
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3
    self.nota4 = nota4

  def media_final(self):
    mf = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    print('\nMédia: {}\n'.format(mf))

    if mf >= 7:
      print('Aprovado')

    elif mf < 5:
      print('Reprovado')
    
    else:
      print('Recuperação')

aux = False
while not aux:
  try: 
    nota1 = float(input('Digite a 1º nota: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

aux = False
while not aux:
  try: 
    nota2 = float(input('Digite a 2º nota: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

aux = False
while not aux:
  try: 
    nota3 = float(input('Digite a 3º nota: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

aux = False
while not aux:
  try: 
    nota4 = float(input('Digite a 4º nota: '))
    aux = True
  except (ValueError):
    print('Valor inválido, tente novamente.')

aluno = Boletim(nota1, nota2, nota3, nota4)

print('\nNota 1: {}'.format(aluno.nota1))
print('Nota 2: {}'.format(aluno.nota2))
print('Nota 3: {}'.format(aluno.nota3))
print('Nota 4: {}'.format(aluno.nota4))

aluno.media_final()