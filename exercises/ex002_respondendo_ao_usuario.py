# Solicita o nome e exibe uma mensagem de apresentação.
nome = input("Digite seu nome:\n").upper()

print("Prazer em te conhecer,\033[4;33;44m", nome + "!\033[0m")
