from estudante import Estudante
from pessoa import Pessoa
from professor import Professor

pessoa1 = Pessoa('Maricota', 28)
pessoa1.apresentar()

print('*' * 10, end='\n')

estudante1 = Estudante('Sansão', 30, 'JavaScript')
estudante1.estudar()

print('*' * 10, end='\n')

professor1 = Professor('Quitéria', 45, 'Matemática')
professor1.dar_aula()