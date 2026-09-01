# Exercício Python #044 - Gerenciador de Pagamentos
# Calcula o valor do produto de acordo com a forma de pagamento e a quantidade de parcelas.

valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Qual é a forma de pagamento?\n1 - Dinheiro ou cheque à vista\n2 - Cartão à vista\n3 - Cartão parcelado\n"))

if forma_pagamento == 1:
    print("Você pagará R$ {:.2f} à vista, em dinheiro ou cheque.".format(valor_produto * 0.9))
elif forma_pagamento == 2:
        print("Você pagará R$ {:.2f} à vista no cartão.".format(valor_produto * 0.95))
elif forma_pagamento == 3:
    quantidade_parcelas = int(input("Informe o número de parcelas desejadas:\n1 vez — sem juros\n2 vezes — sem juros\nAcima de 2 vezes — com juros\n"))
    if quantidade_parcelas <= 0:
        print("Número de parcelas inválido.")
    elif quantidade_parcelas > 2:
        print("Você pagará R$ {:.2f} em {} parcelas com juros.".format(valor_produto * 1.2, quantidade_parcelas))
    else:
        print("Você pagará R$ {:.2f} em {} parcelas sem juros.".format(valor_produto, quantidade_parcelas))
else:
    print("Forma de pagamento \033[1;31minválida\033[0m. Por favor, escolha uma opção entre 1, 2 ou 3.")
    