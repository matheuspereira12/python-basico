from math import trunc

nome = input("Digite seu nome:\n")
print("Olá, {}!\n\nDigite um número e este programa mostrará apenas a sua parte inteira.".format(nome))

numero = float(input("Digite um número:\n"))
parte_inteira = trunc(numero)
print("O número que você digitou foi:\n{}\n\nA parte inteira é:\n{}".format(numero, parte_inteira))
