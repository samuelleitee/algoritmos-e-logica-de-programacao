class Aluno:
    def __init__(self, matricula, pessoa):
        self.__matricula = matricula
        self.__pessoa = pessoa

    def get_matricula(self):
        return self.__matricula
    
    def get_pessoa(self):
        return self.__pessoa