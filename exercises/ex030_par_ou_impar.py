# Verifica se o número informado é par ou ímpar

numero = int(input("Digite um número inteiro qualquer: "))

print("\033[1;32mO número {} é par!\033[0m".format(numero) if numero % 2 == 0 else "\033[1;31mO número {} é ímpar!\033[0m".format(numero))
