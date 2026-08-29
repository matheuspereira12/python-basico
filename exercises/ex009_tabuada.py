# Recebe um número e exibe sua tabuada de 1 a 9.

valor = int(input("Digite um número para ver a tabuada:\n"))
print("\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n\033[1;36m{:>5}\033[0m\n".format(valor * 1, valor * 2, valor * 3, valor * 4, valor * 5, valor * 6, valor * 7, valor * 8, valor * 9))
