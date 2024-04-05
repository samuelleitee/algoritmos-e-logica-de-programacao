numero = []
numerosPositivos = 0

for i in range(6):
    valor = float(input())
    numero.append(valor)

for i in numero:
    if i > 0:
        numerosPositivos += 1

print(f"{numerosPositivos} valores positivos")