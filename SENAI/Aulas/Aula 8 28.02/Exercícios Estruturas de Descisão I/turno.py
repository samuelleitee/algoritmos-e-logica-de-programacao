# Entrada
turno = input('Em qual turno você está? ') 
print('[M] - Matutino\n[V] - Vespertino\n[N] - Noturno')

x = turno.upper()

# Processamento
if x == 'M':

    # Saída
    print('Bom dia!')

elif x == 'V':

    # Saída
    print('Boa tarde!')

elif x == 'N':

    # Saída
    print('Boa noite!')

else: 
    print('Turno inválido')

