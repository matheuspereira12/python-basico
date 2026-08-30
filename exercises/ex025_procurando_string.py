# Verifica se existe o nome "Silva" no nome completo.

nome_completo = str(input("Digite seu nome completo: ")).strip().upper()
print("Seu nome tem 'Silva'? \033[1;36m{}\033[0m.".format("SILVA" in nome_completo))
