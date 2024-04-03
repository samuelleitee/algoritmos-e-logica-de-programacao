usuario = input('Usuário: ')
senha = input('Senha: ')

while usuario == senha:
    print('ERROR: Senha e Usuário iguais')
    usuario = input('Usuário: ')
    senha = input('Senha: ')

print('Login efetuado com sucesso!')