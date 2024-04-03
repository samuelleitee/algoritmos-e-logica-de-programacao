class Professor:
    def __init__(self, disciplina, pessoa):
        self.__disciplina = disciplina
        self.__pessoa = pessoa

    def get_disciplina(self):
        return self.__disciplina
    
    def get_pessoa(self):
        return self.__pessoa