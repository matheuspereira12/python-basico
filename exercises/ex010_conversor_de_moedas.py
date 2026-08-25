# Converte reais para dólares pela cotação de R$ 5,36 por US$ 1,00.


quantia_reais = float(input("Digite quanto você tem em reais (R$):\n"))
print("Você pode comprar US$ {:.2f}.\n".format(quantia_reais / 5.36))
