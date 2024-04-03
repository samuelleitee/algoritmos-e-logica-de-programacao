from televisao import Televisao

televisao1 = Televisao('LG', '4K QLED', 2500, '55"', True)

print('Marca: {}'.format(televisao1.marca))
print('Modelo: {}'.format(televisao1.modelo))
print('Preço: {}'.format(televisao1.preco))
print('Tela: {}'.format(televisao1.tela))
print('Smart: {}'.format(televisao1.smart))

televisao1.ligar()
televisao1.desligar()
televisao1.assistir()