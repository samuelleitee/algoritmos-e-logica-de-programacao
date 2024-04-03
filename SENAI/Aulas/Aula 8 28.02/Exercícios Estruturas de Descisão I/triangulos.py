print('-' * 15)
print('Triângulos')
print('-' * 15)

a = int(input('Medida do primeiro lado: '))
b = int(input('Medida do segundo lado: '))
c = int(input('Medida do terceiro lado: '))

if (a < b + c) and (b < a + c) and (c < a + b):
    print('Triângulo Válido')

    if (a == b) and (a == c) and (b == c):
        print('Triângulo Equilátero')

    elif ((a == b) and (a != c) and (b != c)) or ((a != b) and (a == c) and (b != c)) or ((a != b) and (a != c) and (b == c)):
        print('Triângulo Isósceles')

    else:
        print('Triângulo Escaleno')

else:
    print('Triângulo Inválido')


    # (a != b) and (a != c) and (b != c)