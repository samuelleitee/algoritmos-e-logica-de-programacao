# Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
# menor e o maior, apresentando-os na tela.

numeros = []

while True:
    try: 
        n = int(input("Digite o quantos números serão lidos: "))
        break
    except:
        print("Valor inválido, tente novamente")

for i in range(n):
    while True:
        try:
            numero = float(input("Digite um número: "))

            numeros.append(numero)
            break
        except: 
            print("Valor inválido, tente novamente.")

print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")

# RESOLUÇÃO SEM UTILIZAR LISTAS:

# maior = 0
# menor = 0

# while True:
#     try: 
#         n = int(input("Digite o quantos números serão lidos: "))
#         break
#     except:
#         print("Valor inválido, tente novamente")

# for i in range(n):
#     while True:
#         try:
#             numero = float(input("Digite um número: "))

#             if i == 0:
#                 maior = numero
#                 menor = numero
            
#             if numero > maior:
#                 maior = numero
            
#             if numero < menor:
#                 menor = numero

#             break
#         except: 
#             print("Valor inválido, tente novamente.")

# print(f"Maior: {maior}")
# print(f"Menor: {menor}")

# RESOLUÇÃO ESTILO DO-WHILE

# maior = 0
# menor = 0

# while True:
#     try: 
#         n = int(input("Digite o quantos números serão lidos: "))
#         break
#     except:
#         print("Valor inválido, tente novamente")

# while True:
#     try:
#         numero = float(input("Digite um número: "))
#         break
#     except: 
#         print("Valor inválido, tente novamente.")

# maior = menor = numero

# for i in range(n - 1):
#     while True:
#         try:
#             numero = float(input("Digite um número: "))
            
#             if numero > maior:
#                 maior = numero
            
#             if numero < menor:
#                 menor = numero

#             break
#         except: 
#             print("Valor inválido, tente novamente.")

# print(f"Maior: {maior}")
# print(f"Menor: {menor}")