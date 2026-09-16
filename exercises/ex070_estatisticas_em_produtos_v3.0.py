contador = 0
total_compra = 0
produtos_mais_1000 = 0
produto_mais_barato = None
menor_valor = 0

while True:
    nome_produto = input("Digite o nome do produto: ").strip().upper()
    valor_produto = float(input("Digite o valor do produto: "))
    contador += 1
    total_compra += valor_produto
    if contador == 1:
        produto_mais_barato = nome_produto
        menor_valor = valor_produto
    else:
        if valor_produto < menor_valor:
            produto_mais_barato = nome_produto
            menor_valor = valor_produto
    if valor_produto > 1000:
        produtos_mais_1000 += 1
    while True:
        continuar = input("Deseja continuar? [S/N]: ").strip().upper()
        if continuar == "S" or continuar == "N":
            break
        else:
            print("Digite apenas S ou N.")
    if continuar == "N":
        break
print(f"Total da compra: {total_compra:.2f}. Produto mais barato: {produto_mais_barato}. Quantidade de produtos com valor superior a R$ 1.000,00: {produtos_mais_1000}.")