# Lê o nome completo e exibe o primeiro e o último nome


nome_completo = str(input("Digite seu nome completo: ")).strip().split()
print("É um prazer conhecer você!\nSeu primeiro nome é {} e seu último nome é {}.".format(nome_completo[0].capitalize(), nome_completo[len(nome_completo) - 1].capitalize()))
