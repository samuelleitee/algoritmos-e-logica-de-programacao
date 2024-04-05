numeros = []

for i in range(100):
    numero = int(input())
    numeros.append(numero)

print(max(numeros))
print(numeros.index(max(numeros)) + 1)