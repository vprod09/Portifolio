produtos = {
    1: {"nome": "Coca-cola", "preco": 3.75, "estoque": 2},
    2: {"nome": "Pepsi", "preco": 3.67, "estoque": 5},
    3: {"nome": "Monster", "preco": 9.96, "estoque": 1},
    4: {"nome": "Café", "preco": 1.25, "estoque": 100},
    5: {"nome": "Redbull", "preco": 13.99, "estoque": 2}
}

# Função para calcular o valor do troco
def calcular_troco(valor_pago, preco_produto):
    troco = valor_pago - preco_produto
    notas = [100, 50, 20, 10, 5, 2, 1]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    troco_detalhado = []

    for nota in notas:
        if troco >= nota:
            qtd_notas = int(troco // nota)
            troco_detalhado.append(f"{qtd_notas} nota(s) de R${nota}")
            troco -= qtd_notas * nota

    for moeda in moedas:
        if troco >= moeda:
            qtd_moedas = int(troco // moeda)
            troco_detalhado.append(f"{qtd_moedas} moeda(s) de R${moeda:.2f}")
            troco -= qtd_moedas * moeda

    return troco_detalhado

# Função principal da máquina de bebidas
def maquina_de_bebidas():
    while True:
        print("\nBem-vindo à Máquina de Bebidas!")
        print("Produtos disponíveis:")
        for id, produto in produtos.items():
            print(f"{id}: {produto['nome']} - R${produto['preco']} - Estoque: {produto['estoque']}")

        codigo = int(input("\nDigite o código do produto desejado (ou 0 para sair): "))

        if codigo == 0:
            print("\nObrigado por utilizar nossa máquina. Volte sempre!")
            break

        if codigo not in produtos:
            print("\nCódigo de produto inválido. Tente novamente.")
            continue

        produto_selecionado = produtos[codigo]
        if produto_selecionado['estoque'] == 0:
            print("\nDesculpe, este produto está fora de estoque.")
            continue

        print(f"\nProduto selecionado: {produto_selecionado['nome']}")
        print(f"Valor do produto: R${produto_selecionado['preco']:.2f}")

        valor_pago = float(input("Por favor, insira o valor pago: "))
        while valor_pago < produto_selecionado['preco']:
            print("Valor insuficiente. Por favor, insira um valor igual ou maior ao preço do produto.")
            valor_pago = float(input("Por favor, insira o valor pago: "))

        troco_detalhado = calcular_troco(valor_pago, produto_selecionado['preco'])
        print("\nTroco a ser devolvido:")
        for item in troco_detalhado:
            print(item)

        produto_selecionado['estoque'] -= 1
        print("\nCompra realizada com sucesso!")

# Executando a máquina de bebidas
maquina_de_bebidas()