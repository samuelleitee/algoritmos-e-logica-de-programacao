nota = float(input('Digite uma nota (entre 0 e 10): '))

while not (nota >= 0 and nota <= 10): 
    print('Valor inválido.')
    nota = float(input('Digite a nota novamente (entre 0 e 10): '))

print('Fim do programa.')