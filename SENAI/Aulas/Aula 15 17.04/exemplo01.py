matrizA = [[1,2], [3,4]]
matrizB = [[5,6], [7,8]]
matrizC = [[0,0], [0,0]]

for linha in range(len(matrizA)):
    for coluna in range(len(matrizB)):
        matrizC[linha][coluna] = matrizA[linha][coluna] * matrizB[linha][coluna]

print(matrizC)