from array import *

def somar(vet):
   return sum(vet)

vetor = array('i', [1, 2, 3, 4, 5])

print('A soma é: {}'.format(somar(vetor)))

print(*vetor)