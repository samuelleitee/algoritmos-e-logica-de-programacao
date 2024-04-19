# Reescreva um programa do exercício acima considerando exclusivamente os números positivos
# fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
# "número inválido" e o valor deve ser ignorado.

# ESSA ABORDAGEM OBRIGA QUE O USUÁRIO DIGITE O VALOR NOVAMENTE CASO SEJA INVÁLIDO 

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

# ESSA ABORDAGEM APENAS IGNORA OS VALORES INVÁLIDOS E, CASO TODOS SEJAM INVÁLIDOS, RETORNA UMA RESPOSTA DIZENDO QUE APENAS VALORES INVÁLIDOS FORAM INFORMADOS

# numeros = []

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

#             if numero > 0:
#                 numeros.append(numero)
#             else:
#                 print("Valor inválido.")
#             break
#         except: 
#             print("Valor inválido, tente novamente.")

# print(f"Maior: {max(numeros)}")
# print(f"Menor: {min(numeros)}")