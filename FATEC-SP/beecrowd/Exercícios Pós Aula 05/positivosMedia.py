# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

numero = []
numerosPositivos = 0
somaNumerosPositivos = 0

for i in range(6):
    valor = float(input())
    numero.append(valor)

for i in numero:
    if i > 0:
        numerosPositivos += 1
        somaNumerosPositivos += i

media = somaNumerosPositivos / numerosPositivos

print(f"{numerosPositivos} valores positivos")
print(f"{media:.1f}")