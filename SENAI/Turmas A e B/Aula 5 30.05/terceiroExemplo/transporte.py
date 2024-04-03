class Transporte:
    def __init__(self, nome, velocidade):
        self.__nome = nome
        self.__velocidade = velocidade

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_velocidade(self):
        return self.__velocidade
    
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade

    def mover(self):
        print(f'{self.__nome} está se movendo com velocidade {self.__velocidade}.')

    def parar(self):
        print(f'{self.__nome} está parando.')