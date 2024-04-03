nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('\n1° nota: {:.2f}\n2° nota: {:.2f}\n3° nota: {:.2f}\n4°nota: {:.2f}\n\nMédia final: {:.2f}'. format(nota1, nota2, nota3, nota4, media))

if media >= 9 and media <= 10:
    print('\nConceito: A\nAPROVADO')

elif media >= 7.5 and media <= 8.9:
    print('\nConceito: B\nAPROVADO')

elif media >= 6.0 and media <= 7.4:
    print('\nConceito: C\nAPROVADO')

elif media >= 4.0 and media <= 5.9:
    print('\nConceito: D\nREPROVADO')

elif media >= 0 and media <= 3.9:
    print('\nConceito: E\nREPROVADO')

print('-' * 10)
