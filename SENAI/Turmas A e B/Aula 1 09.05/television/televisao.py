class Televisao:
    def __init__(self, marca, modelo, preco, tela, smart):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.tela = tela
        self.smart = smart

    def ligar(self):
        print('Estou ligando...')

    def desligar(self):
        print('Estou desligando...')

    def assistir(self):
        print('Estou assistindo...')