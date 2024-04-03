from array import array

turma = []

aux = False
while not aux:
    try:
        count = int(input('Digite quantos alunos: '))
        if count > 0:
            aux = True
        else:
            print('Valor inválido, tente novamente.')
    except (ValueError):
        print('Valor inválido, tente novamente.')

# Solicitação dos dados de cada aluno
for i in range(count):
    nome = input('Digite o nome do {}º aluno: '.format(i + 1))
    idade = int(input('Digite a idade do {}º aluno: '.format(i + 1)))
    nota = int(input('Digite a nota do {}º aluno: '.format(i + 1)))
    aluno = [nome, idade, nota]
    turma.append(aluno)

print('\nNome\t\tIdade\tNota')
for i in range(count):
    print(f'{turma[i][0]}\t\t{turma[i][1]}\t{turma[i][2]}')

# Cálculo da média
notas = []
for i in range(count):
    notas.append(turma[i][2])

media = sum(notas) / len(notas)
print(media)