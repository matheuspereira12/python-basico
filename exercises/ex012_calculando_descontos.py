# Calcula o valor final do produto aplicando 5% de desconto

valor_produto = float(input("Digite o valor do produto: R$ "))
desconto = valor_produto * 0.95
print("O valor final com desconto é: R$ \033[1;32m{:.2f}\033[0m.".format(desconto))
