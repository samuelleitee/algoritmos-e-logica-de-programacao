class Celular:
    def __init__(self, marca, modelo, preco, so, tela):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.so = so
        self.tela = tela

    def ligar(self):
        print('Estou ligando...')

    def desligar(self):
        print('Estou desligando...')

    def telefonar(self):
        print('Estou telefonando...')
        
    def jogar(self):
        print('Estou desligando...')