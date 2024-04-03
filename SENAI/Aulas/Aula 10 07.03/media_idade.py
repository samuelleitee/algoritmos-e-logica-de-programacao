p = int(input('Há quantas pessoas na turma? '))

# Validação da quantidade de pessoas
while p <= 0:
    p = int(input('Número inválido, tente novamente: '))

lista = []
count = 1

for i in range(1, p + 1):
    print('Digite a idade da {}º pessoa.'.format(count))
    idade = int(input('Idade: '))
    lista.append(idade)
    count += 1

print('Média: {}'.format(sum(lista) / p))

if sum(lista) / p >= 0 and sum(lista) / p <= 25:
    print('Turma jovem!')
elif sum(lista) / p >= 26 and sum(lista) / p <= 60:
    print('Turma Adulta!')
else:
    print('Idosos!')
