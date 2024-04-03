class Funcionario:
    def __init__(self, nome, idade, salario_base):
        self.nome = nome
        self.idade = idade
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base


class Gerente(Funcionario):
    def __init__(self, nome, idade, salario_base, bonificacao):
        super().__init__(nome, idade, salario_base)
        self.bonificacao = bonificacao

    def calcular_salario(self):
        return self.salario_base + self.bonificacao


class Vendedor(Funcionario):
    def __init__(self, nome, idade, salario_base, comissao, vendas):
        super().__init__(nome, idade, salario_base)
        self.comissao = comissao
        self.vendas = vendas

    def calcular_salario(self):
        return self.salario_base + (self.comissao * self.vendas)


def imprimir_salario(Funcionario):
    print(f"El salario de {Funcionario.nome} es: {Funcionario.calcular_salario()}")


if __name__ == "__main__":
    Funcionario1 = Funcionario("Pedro", 30, 2000)
    gerente1 = Gerente("María", 40, 3000, 1000)
    vendedor1 = Vendedor("Juan", 25, 1500, 0.1, 5000)

    imprimir_salario(Funcionario1)
    imprimir_salario(gerente1)
    imprimir_salario(vendedor1)