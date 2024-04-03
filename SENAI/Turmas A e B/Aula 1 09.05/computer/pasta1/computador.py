class MeuComputador:
    def __init__(self, marca, modelo, preco, placa_mae, processador, gabinete, fonte, monitor):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.placa_mae = placa_mae
        self.processador = processador
        self.gabinete = gabinete
        self.fonte = fonte
        self.monitor = monitor

    def ligar(self):
        print('Estou ligando...')

    def desligar(self):
        print('Estou desligando...')

    def jogar(self):
        print('Estou jogando...')

    def estudar(self):
        print('Estou estudando...')