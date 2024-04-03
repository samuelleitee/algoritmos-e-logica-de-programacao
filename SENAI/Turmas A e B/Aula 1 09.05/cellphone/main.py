from celular import *

celular1 = Celular('Samsung', 'S9', 1000, 'Android 10', '5.8"')

print('Marca: {}'.format(celular1.marca))
print('Modelo: {}'.format(celular1.modelo))
print('Preço: {}'.format(celular1.preco))
print('Sistema operacional: {}'.format(celular1.so))
print('Tela: {}'.format(celular1.tela))

celular1.ligar()
celular1.desligar()
celular1.telefonar()
celular1.jogar()