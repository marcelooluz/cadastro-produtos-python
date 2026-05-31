produtos = {}

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Alterar preço")
    print("5 - Remover produto")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        produtos[nome] = preco
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        if len(produtos) == 0:
            print("Nenhum produto cadastrado.")
        else:
            print("\nProdutos cadastrados:")
            for nome, preco in produtos.items():
                print(f"{nome} - R$ {preco:.2f}")

    elif opcao == "3":
        nome = input("Digite o nome do produto: ")

        if nome in produtos:
            print(f"{nome} - R$ {produtos[nome]:.2f}")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        nome = input("Produto que deseja alterar: ")

        if nome in produtos:
            novo_preco = float(input("Novo preço: R$ "))
            produtos[nome] = novo_preco
            print("Preço atualizado!")
        else:
            print("Produto não encontrado.")

    elif opcao == "5":
        nome = input("Produto que deseja remover: ")

        if nome in produtos:
            del produtos[nome]
            print("Produto removido!")
        else:
            print("Produto não encontrado.")

    elif opcao == "6":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")
