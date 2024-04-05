# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

numero = []
pares = 0

for i in range(5):
    valor = int(input())
    numero.append(valor)

for i in numero:
    if i % 2 == 0:
        pares += 1

print(f"{pares} valores pares", end="\n")