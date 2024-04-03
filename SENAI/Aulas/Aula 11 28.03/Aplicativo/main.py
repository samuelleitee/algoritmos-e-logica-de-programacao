from compras import adicionar_item, remover_item, mostrar_lista

# Definir a lista de compras
compras = []

# Loop principal da aplicação
while True:
    # Mostrar as opções do menu
    print('Selecione uma opção: ')
    print('1 - Adicionar item à lista de compras')
    print('2 - Remover item da lista de compras')
    print('3 - Mostrar os itens da lista de compras')
    print('4 - Sair')

    # Ler a opção do menu selecionada pelo usuário
    opcao = int(input('Opção selecionada: '))

    if opcao == 1:
        # Adicionar item à lista de compras
        item = input('Digite o item a ser adicionado na lista de compras: ')
        adicionar_item(compras, item)
    
    elif opcao == 2:
        # Remover item da lista de compras
        if len(compras) == 0:
            print('Não há itens na lista de compras.')
        else:
            item = input('Digite um item a ser removido da lista de compras: ')
            remover_item(compras, item)

    elif opcao == 3:
        # Mostrar os itens da lista de compras
        mostrar_lista(compras)

    elif opcao == 4:
        # Sair do aplicativo
        print('Saindo...')

    else:
        # Mostrar uma mensagem de erro se a opção não for válida
        print('Opção inválida, tente novamente.')