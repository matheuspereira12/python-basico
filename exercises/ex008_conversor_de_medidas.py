# Converte o valor em metros para as demais unidades de medida.

valor_metros = int(input("Digite um valor em metros:\n"))
print("O valor de \033[1;36m{:.2f}\033[0m metros equivale a:\n\033[1;34m{:.2f}\033[0m quilômetros\n\033[34m{:.2f}\033[0m hectômetros\n\033[1;32m{:.2f}\033[0m decâmetros\n\033[32m{:.2f}\033[0m decímetros\n\033[1;33m{:.2f}\033[0m centímetros\n\033[33m{:.2f}\033[0m milímetros".format(valor_metros, (valor_metros / 1000), (valor_metros / 100), (valor_metros / 10), (valor_metros * 10), (valor_metros * 100), (valor_metros * 1000)))
