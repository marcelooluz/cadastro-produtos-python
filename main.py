produtos = {}

while True:
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        preco = float(input("Preço: R$ "))
        produtos[nome] = preco

    elif opcao == "2":
        for nome, preco in produtos.items():
            print(f"{nome} - R$ {preco:.2f}")

    elif opcao == "3":
        break