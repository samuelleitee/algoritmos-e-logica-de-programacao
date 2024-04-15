# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

casosDeTeste = int(input())
somas = []

for i in range(casosDeTeste):
    x, y = map(int, input().split())
    soma = 0

    if x < y:
        for i in range(x + 1, y):
            if i % 2 != 0: 
                soma += i

    else: 
        for i in range(y + 1, x):
            if i % 2 != 0: 
                soma += i

    somas.append(soma)
    
for soma in somas:
    print(soma)
