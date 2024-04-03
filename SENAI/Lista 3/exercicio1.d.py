pares = []

for i in range(501):
    if i % 2 == 0:
        pares.append(i)

print(*pares, sep=' + ', end=' = ')
print(sum(pares))