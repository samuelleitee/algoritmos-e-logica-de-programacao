from transporte import Transporte

class Terrestre(Transporte):
    def __init__(self, nome, velocidade, num_rodas):
        super().__init__(nome, velocidade)
        self.__num_rodas = num_rodas

    def get_num_rodas(self):
        return self.__num_rodas
    
    def set_num_rodas(self):
        return self.__num_rodas

    def fazer_curva(self):
        print(f'{self._Transporte__nome} está fazendo curva a {self._Transporte__velocidade} Km/h.')