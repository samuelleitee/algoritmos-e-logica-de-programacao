# Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
# para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):
# 4 x 1 = 4
# 4 x 2 = 8
# 4 x 3 = 12
# ...
# 4 x 10 = 40

while True:
    try:
        n = int(input("Digite o número que você deseja saber a tabuada: "))
        break
    except: 
        print("Valor inválido, tente novamente.")

for i in range(11):
    print(f"{i:2} x {n:1} = {i * n:2}") # var:2 serve para indicar quantas colunas o resultado irá ocupar no terminal