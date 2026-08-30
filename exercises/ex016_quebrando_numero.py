from math import trunc

nome = input("Digite seu nome:\n")
print("Olá, \033[1;36m{}\033[0m!\n\nDigite um número e este programa mostrará apenas a sua parte inteira.".format(nome))

numero = float(input("Digite um número:\n"))
parte_inteira = trunc(numero)
print("O número que você digitou foi:\n\033[1;32m{}\033[0m\n\nA parte inteira é:\n\033[1;32m{}\033[0m.".format(numero, parte_inteira))
