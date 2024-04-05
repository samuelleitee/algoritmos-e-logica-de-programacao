# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

n = int(input())
medias = []

for valor in range(n):
    primeiro = float(input())
    segundo = float(input())
    terceiro = float(input())

    media = (2 * primeiro + 3 * segundo + 5 * terceiro) / (2 + 3 + 5) 
    medias.append(media)

for media in medias:
    print(f"{media:.1f}", end="\n")