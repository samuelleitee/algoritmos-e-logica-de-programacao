num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro diferente: '))
num3 = int(input('Digite mais um número inteiro diferente: '))

if (num1 > num2) and (num1 > num3) and (num2 > num3):
    print('Maior: {}\nMenor: {}'.format(num1, num3))

elif (num1 > num2) and (num1 > num3) and (num3 > num2):
    print('Maior: {}\nMenor: {}'.format(num1, num2))

elif (num2 > num1) and (num2 > num3) and (num1 > num3):
    print('Maior: {}\nMenor: {}'.format(num2, num3))

elif (num2 > num1) and (num2 > num3) and (num3 > num1):
    print('Maior: {}\nMenor: {}'.format(num2, num1))

elif (num3 > num1) and (num3 > num2) and (num1 > num2):
    print('Maior: {}\nMenor: {}'.format(num3, num2))

elif (num3 > num1) and (num3 > num2) and (num2 > num1):
    print('Maior: {}\nMenor: {}'.format(num3, num1))
else: 
    print('Digite números diferentes.')