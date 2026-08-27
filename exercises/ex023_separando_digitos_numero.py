# Exercício realizado utilizando strings para separar os dígitos do número informado.


numero = str(input("Digite um número de 0 a 9999: ")).strip()


print("Milhares: {}\nCentenas: {}\nDezenas: {}\nUnidades: {}".format(numero[0], numero[1], numero[2], numero[3]))
