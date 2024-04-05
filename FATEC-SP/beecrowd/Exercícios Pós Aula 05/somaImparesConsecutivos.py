# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

x = int(input())
y = int(input())
soma = 0

if x < y:
    for i in range(x + 1 , y):
        if i % 2 != 0:
            soma += i

else: 
    for i in range(y + 1, x):
        if i % 2 != 0:
            soma += i

print(soma, end="\n")