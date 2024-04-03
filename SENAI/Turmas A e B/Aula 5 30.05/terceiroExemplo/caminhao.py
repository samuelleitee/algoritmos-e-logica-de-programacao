from terrestre import Terrestre

class Caminhao(Terrestre):
    def __init__(self, carga, velocidade):
        super().__init__('Caminhão', velocidade, 18)
        self.__carga = carga

    def get_carga(self):
        return self.__carga
    
    def set_carga(self, carga):
        self.__carga = carga

    def transportar(self):
        print(f'{self.get_nome()} está transportando {self.get_carga()} t.')