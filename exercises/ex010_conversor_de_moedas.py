# Converte reais para dólares pela cotação de R$ 5,36 por US$ 1,00.


quantia_reais = float(input("Digite quanto você tem em reais (R$):\n"))
print("Você pode comprar US$ \033[1;32m{:.2f}\033[0m.".format(quantia_reais / 5.36))
