# Converte o valor em metros para as demais unidades de medida.

valor_metros = int(input("Digite um valor em metros:\n"))
print("O valor de {:.2f} metros equivale a:\n{:.2f} quilômetros\n{:.2f} hectômetros\n{:.2f} decâmetros\n{:.2f} decímetros\n{:.2f} centímetros\n{:.2f} milímetros\n".format(valor_metros, (valor_metros / 1000), (valor_metros / 100), (valor_metros / 10), (valor_metros * 10), (valor_metros * 100), (valor_metros * 1000)))
