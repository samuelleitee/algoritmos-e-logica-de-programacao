from pessoa import Pessoa
from estudante import Estudante

pessoa1 = Pessoa('Owaldo', 30)
pessoa1.apresentar()

print('*' * 10, end='\n')

estudante1 = Estudante('Fulano', 35, 'Python')
estudante1.apresentar()