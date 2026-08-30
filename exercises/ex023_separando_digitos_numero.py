# Exercício realizado utilizando strings para separar os dígitos do número informado.


numero = str(input("Digite um número de 0 a 9999: ")).strip()


print("Milhares: \033[1;31m{}\033[0m\nCentenas: \033[1;33m{}\033[0m\nDezenas: \033[1;32m{}\033[0m\nUnidades: \033[1;34m{}\033[0m".format(numero[0], numero[1], numero[2], numero[3]))
