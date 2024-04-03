from aereo import Aereo

class Aviao_Carga(Aereo):
    def __init__(self, carga, velocidade):
        super().__init__('Avião de carga', velocidade, 13000)
        self.__carga = carga

    def get_carga(self):
        return self.__carga
    
    def set_carga(self, carga):
        self.__carga = carga

    def carregar(self):
        print(f'Estamos carregando o {self.get_nome()}')