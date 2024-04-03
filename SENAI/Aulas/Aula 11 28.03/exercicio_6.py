import random

lista = []
count = 1

while count <= 500:
    number = random.randint(1, 5000)
    lista.append(number)
    count += 1
    
lista.sort()
print(*lista, sep=', ')