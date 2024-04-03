from aluno import Aluno
from pessoa import Pessoa
from professor import Professor

# print('\n' + '*' * 12 + '\n')
pessoa1 = Pessoa('Fulano', 1, 'Lugar 1')
pessoa2 = Pessoa('Ciclano', 2, 'Lugar 2')

aluno1 = Aluno(11, pessoa1)
aluno2 = Aluno(22, pessoa2)

professor1 = Professor('Matemática', pessoa1)
professor2 = Professor('Português', pessoa2)

print('Dados do aluno 1')
print(f'Nome: {pessoa1.get_nome()}')
print(f'Idade: {pessoa1.get_idade()}')
print(f'Endereço: {pessoa1.get_endereco()}')
print(f'Matrícula: {aluno1.get_matricula()}')

print('\n' + '*' * 12 + '\n')

print('Dados do aluno 2')
print(f'Nome: {pessoa2.get_nome()}')
print(f'Idade: {pessoa2.get_idade()}')
print(f'Endereço: {pessoa2.get_endereco()}')
print(f'Matrícula: {aluno2.get_matricula()}')

print('\n' + '*' * 12 + '\n')

print('Dados do professor 1')
print(f'Nome: {pessoa1.get_nome()}')
print(f'Idade: {pessoa1.get_idade()}')
print(f'Endereço: {pessoa1.get_endereco()}')
print(f'Disciplina: {professor1.get_disciplina()}')

print('\n' + '*' * 12 + '\n')

print('Dados do professor 2')
print(f'Nome: {pessoa2.get_nome()}')
print(f'Idade: {pessoa2.get_idade()}')
print(f'Endereço: {pessoa2.get_endereco()}')
print(f'Disciplina: {professor2.get_disciplina()}')