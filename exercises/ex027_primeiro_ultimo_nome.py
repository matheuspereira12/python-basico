# Lê o nome completo e exibe o primeiro e o último nome


nome_completo = str(input("Digite seu nome completo: ")).strip().split()
print("É um prazer conhecer você!\nSeu primeiro nome é \033[1;32m{}\033[0m e seu último nome é \033[1;36m{}\033[0m.".format(nome_completo[0].capitalize(), nome_completo[len(nome_completo) - 1].capitalize()))
