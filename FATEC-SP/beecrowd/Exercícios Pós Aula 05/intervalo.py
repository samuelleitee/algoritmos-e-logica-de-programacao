# Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
# Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

n = int(input())
numeros = []
intervalo = 0

for i in range(n):
    valor = int(input())
    numeros.append(valor)

for i in numeros:
    if i >= 10 and i <= 20:
        intervalo += 1

print(f"{intervalo} in", end="\n")
print(f"{len(numeros) - intervalo} out", end="\n")