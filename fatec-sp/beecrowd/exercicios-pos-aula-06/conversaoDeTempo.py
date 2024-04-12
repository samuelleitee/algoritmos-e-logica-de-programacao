# Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

# Entrada
# O arquivo de entrada contém um valor inteiro N.

# Saída
# Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.

duracaoSegundos = int(input())

horas = 0
minutos = 0
segundos = 0

if duracaoSegundos / 3600 > 0:
    horas = int(duracaoSegundos / 3600)
    duracaoSegundos -= horas * 3600

if duracaoSegundos / 60 > 0:
    minutos = int(duracaoSegundos / 60)
    duracaoSegundos -= minutos * 60

segundos = duracaoSegundos

print(f"{horas}:{minutos}:{segundos}", end="\n")