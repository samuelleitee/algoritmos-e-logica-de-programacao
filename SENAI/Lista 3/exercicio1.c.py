lista = []

for i in range(1, 101):  
    lista.append(i)

print(*lista, sep=' + ', end=' = {}'.format(sum(lista))) 