# Verifica se o número informado é par ou ímpar

numero = int(input("Digite um número inteiro qualquer: "))

print("O número {} é par!".format(numero) if numero % 2 == 0 else "O número {} é ímpar!".format(numero))
