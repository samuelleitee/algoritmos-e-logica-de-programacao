nome = input('Nome: ')

while len(nome) <= 3:
    nome = input('O nome deve ter mais que 3 caracteres, tente novamente: ')

idade = int(input('Idade: '))

while idade < 0 or idade > 150:
    idade = int(input('A idade deve estar entre 0 e 150, tente novamente: '))

salario = float(input('Salário: R$'))

while salario <= 0:
    salario = float(input('O salário deve ser maior que R$00.00, tente novamente: '))

sexo = input('Sexo ([F] Feminino [M] Masculino): ')
x = sexo.upper()

while x != 'F' and x != 'M':
    sexo = input('Sexo inválido, tente novamente ([F] Feminino [M] Masculino): ')
    x = sexo.upper()

estadoCivil = input('Estado civil ([S] Solteiro [C] Casado [V] Viúvo [D] Divorciado): ')
y = estadoCivil.upper()

while y != 'S' and y != 'C' and y != 'V' and y != 'D':
    estadoCivil = input('Estado civil ([S] Solteiro [C] Casado [V] Viúvo [D] Divorciado): ')
    y = estadoCivil.upper()

print('Login efetuado com sucesso!\nNome: {}\nIdade: {}\nSalário: {:.2f}\nSexo: {}\nEstado civil: {}'.format(nome, idade, salario, x, y))