# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

n = int(input())
aux = 0

# cedulas[0] = cédulas de 1
# cedulas[1] = cédulas de 2
# cedulas[2] = cédulas de 5
# cedulas[3] = cédulas de 10
# cedulas[4] = cédulas de 20
# cedulas[5] = cédulas de 50
# cedulas[6] = cédulas de 100

cedulas = [0, 0, 0, 0, 0, 0, 0]

print(f"{n}", end="\n")

if n // 100:
    cedulas[6] = n // 100
    n -= (n // 100) * 100

if n // 50:
    cedulas[5] = n // 50
    n -= (n // 50) * 50

if n // 20:
    cedulas[4] = n // 20
    n -= (n // 20) * 20

if n // 10:
    cedulas[3] = n // 10
    n -= (n // 10) * 10

if n // 5:
    cedulas[2] = n // 5
    n -= (n // 5) * 5

if n // 2:
    cedulas[1] = n // 2
    n -= (n // 2) * 2

if n // 1:
    cedulas[0] = n // 1
    n -= (n // 1) * 1

print(f"{cedulas[6]} nota(s) de R$ 100,00", end="\n")
print(f"{cedulas[5]} nota(s) de R$ 50,00", end="\n")
print(f"{cedulas[4]} nota(s) de R$ 20,00", end="\n")
print(f"{cedulas[3]} nota(s) de R$ 10,00", end="\n")
print(f"{cedulas[2]} nota(s) de R$ 5,00", end="\n")
print(f"{cedulas[1]} nota(s) de R$ 2,00", end="\n")
print(f"{cedulas[0]} nota(s) de R$ 1,00", end="\n")