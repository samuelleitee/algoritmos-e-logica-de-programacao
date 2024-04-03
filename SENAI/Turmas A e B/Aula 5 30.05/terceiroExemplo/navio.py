from maritmo import Maritmo

class Navio(Maritmo):
    def __init__(self, carga, velocidade):
        super().__init__('Navio', velocidade, 100)
        self.__carga = carga

    def get_carga(self):
        return self.__carga
    
    def set_carga(self, carga):
        self.__carga = carga

    def carregar(self):
        print(f'{self.get_nome()} carregando {self.__carga} toneladas.')