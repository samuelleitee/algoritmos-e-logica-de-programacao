from pessoa import Pessoa

class Estudante(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade) #super indica a classe base que é herdada.
        self.curso = curso

    def estudar(self):
        super().apresentar()
        print(f'Estou estudando {self.curso}.')