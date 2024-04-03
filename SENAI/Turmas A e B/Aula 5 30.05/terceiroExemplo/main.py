from transporte import Transporte
from terrestre import Terrestre
from maritmo import Maritmo
from aereo import Aereo
from carro import Carro
from caminhao import Caminhao
from navio import Navio
from barco import Barco
from aviao_passageiro import Aviao_Passageiro
from aviao_carga import Aviao_Carga

transporte1 = Transporte('Carro', 200)
transporte1.mover()
transporte1.parar()

terrestre1 = Terrestre('Carro', 180, 4)
terrestre1.mover()
terrestre1.parar()
terrestre1.fazer_curva()

maritmo1 = Maritmo('Lancha', 100, 10)
maritmo1.mover()
maritmo1.parar()
maritmo1.transportar_passageiros()

aereo1 = Aereo('Boing', 200, 15000)
aereo1.voar_altitude()

carro1 = Carro('GM', 100)
carro1.fazer_curva()
carro1.buzinar()

caminhao1 = Caminhao(10, 20)
caminhao1.fazer_curva()
caminhao1.transportar()

navio1 = Navio(10000, 50)
navio1.carregar()

barco1 = Barco(100, 30)
barco1.embarcar_pessoas()

aviao_passageiro1 = Aviao_Passageiro(200, 350)
aviao_passageiro1.decolar()

aviao_carga1 = Aviao_Carga(5000, 500)
aviao_carga1.carregar()