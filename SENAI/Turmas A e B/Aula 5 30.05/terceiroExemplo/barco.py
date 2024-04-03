from maritmo import Maritmo

class Barco(Maritmo):
    def __init__(self, velocidade, num_passageiros):
        super().__init__('Barco', velocidade, num_passageiros)

    def embarcar_pessoas(self):
        print(f'Embarcando {self._Maritmo__num_passageiros} pessoas no {self.get_nome()}.')