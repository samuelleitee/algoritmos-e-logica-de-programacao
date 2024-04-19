# Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
# mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
# mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.:

while True:
    try:
        minimo = int(input("Escreva o valor mínimo: "))
        break
    except: 
        print("Valor inválido, tente novamente.")

while True:
    try:
        maximo = int(input("Escreva o valor máximo: "))

        if maximo <= minimo:
            print("O valor máximo deve ser maior que o mínimo, tente novamente.")
        else:
            break
    except: 
        print("Valor inválido, tente novamente.")

for numero in range(minimo + 1, maximo):
    if numero % 5 == 0:
        print(numero)    