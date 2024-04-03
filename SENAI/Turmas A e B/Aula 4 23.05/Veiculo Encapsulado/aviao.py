class Aviao:
    def __init__(self, num_assentos, veiculo):
        self.__num_assentos = num_assentos
        self.__veiculo = veiculo

    def get_num_assentos(self):
        return self.__num_assentos
    
    def get_veiculo(self):
        return self.__veiculo

    def decolar(self):
        print('Estou decolando!')