from transporte import Transporte

class Maritmo(Transporte):
    def __init__(self, nome, velocidade, num_passageiros):
        super().__init__(nome, velocidade)
        self.__num_passageiros = num_passageiros

    def get_num_passageiros(self):
        return self.__num_passageiros
    
    def set_num_passageiros(self, num_passageiros):
        self.__num_passageiros = num_passageiros

    def transportar_passageiros(self):
        print(f'{self.get_nome()} transportando {self.__num_passageiros} passageiros.')
