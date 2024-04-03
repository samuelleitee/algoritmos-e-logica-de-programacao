from veiculo import Veiculo
from aviao import Aviao
from carro import Carro

veiculo1 = Veiculo('Marca1', 'Modelo1', 2021)
veiculo2 = Veiculo('Marca2', 'Modelo2', 2022)

carro1 = Carro(5, veiculo1)
carro2 = Carro(3, veiculo2)

aviao1 = Aviao(300, veiculo1)
aviao2 = Aviao(30, veiculo2)

print('Dados do carro 1')
print(f'Marca: {veiculo1.get_marca()}')
print(f'Modelo: {veiculo1.get_modelo()}')
print(f'Ano: {veiculo1.get_ano()}')
print(f'Portas: {carro1.get_num_portas()}')

print('\n' + '*' * 12 + '\n')

print('Dados do carro 2')
print(f'Marca: {veiculo2.get_marca()}')
print(f'Modelo: {veiculo2.get_modelo()}')
print(f'Ano: {veiculo2.get_ano()}')
print(f'Portas: {carro2.get_num_portas()}')

print('\n' + '*' * 12 + '\n')

print('Dados do avião 1')
print(f'Marca: {veiculo1.get_marca()}')
print(f'Modelo: {veiculo1.get_modelo()}')
print(f'Ano: {veiculo1.get_ano()}')
print(f'Assentos: {aviao1.get_num_assentos()}')

print('\n' + '*' * 12 + '\n')

print('Dados do avião 2')
print(f'Marca: {veiculo2.get_marca()}')
print(f'Modelo: {veiculo2.get_modelo()}')
print(f'Ano: {veiculo2.get_ano()}')
print(f'Assentos: {aviao2.get_num_assentos()}')