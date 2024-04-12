# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

numero = []
numerosPositivos = 0
numerosNegativos = 0
numerosPares = 0
numerosImpares = 0

for i in range(5):
    valor = int(input())
    numero.append(valor)

for i in numero:
    if i > 0:
        numerosPositivos += 1
    elif i < 0:
        numerosNegativos += 1

    if i % 2 == 0:
        numerosPares += 1
    else:
        numerosImpares += 1


print(f"{numerosPares} valor(es) par(es)")
print(f"{numerosImpares} valor(es) impar(es)")
print(f"{numerosPositivos} valor(es) positivo(s)")
print(f"{numerosNegativos} valor(es) negativo(s)")