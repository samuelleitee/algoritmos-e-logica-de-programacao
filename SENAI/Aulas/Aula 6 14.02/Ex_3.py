a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite mais um valor: '))

if (a > b) and (a > c) and (b > c):
    print("Ordem crescente: {}; {}; {}".format(c, b, a))
elif (a > b) and (a > c) and (c > b):
    print("Ordem crescente: {}; {}; {}".format(b, c, a))
elif (b > a) and (b > c) and (c > a):
    print("Ordem crescente: {}; {}; {}".format(a, c, b))
elif (b > a) and (b > c) and (a > c):
    print("Ordem crescente: {}; {}; {}".format(c, a, b))
elif (c > a) and (c > b) and (b > a):
    print("Ordem crescente: {}; {}; {}".format(a, b, c))
elif (a == b) and (a == c) and (b == c):
    print('Os valores são iguais: {}={}={}'.format(a, b, c))
else:
    print("Ordem crescente: {}; {}; {}".format(b, a, c))

    # 5; 6; 4