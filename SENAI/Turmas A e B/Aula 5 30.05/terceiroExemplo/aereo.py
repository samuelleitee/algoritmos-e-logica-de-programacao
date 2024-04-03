from transporte import Transporte

class Aereo(Transporte):
    def __init__(self, nome, velocidade, altitude):
        super().__init__(nome, velocidade)
        self.__altitude = altitude

    def get_altitude(self):
        return self.__altitude
    
    def set_altitude(self, altitude):
        self.__altitude = altitude

    def voar_altitude(self):
        print(f'{self.get_nome()} está voando a {self.__altitude} ft.')
        print(f'{self._Transporte__nome} está voando a {self._Transporte__velocidade} km/h.')