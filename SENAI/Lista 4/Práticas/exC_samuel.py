from array import *

matrizA = array('f', [20., 19., 18., 17., 16., 15., 14., 13., 12., 11., 10., 9., 8., 7., 6., 5., 4., 3., 2., 1.])
matrizB = array('f', [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12., 13., 14., 15., 16., 17., 18., 19., 20.])
matrizC = array('f', [])

for i in range(0, 20):
    subtracao = matrizA[i] - matrizB[i]
    matrizC.append(subtracao)

print(matrizC)