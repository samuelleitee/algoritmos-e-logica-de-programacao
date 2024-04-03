class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.__nome = nome
        self.__idade = idade
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def get_endereco(self):
        return self.__endereco