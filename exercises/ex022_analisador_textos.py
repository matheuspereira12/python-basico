# Solicita o nome completo e exibe informações sobre ele, como maiúsculas, minúsculas e quantidade de letras.

nome_completo = input("Digite seu nome completo:\n").strip()

print("Seu nome com letras maiúsculas é \033[1;34m{}\033[0m\nSeu nome com letras minúsculas é \033[1;32m{}\033[0m\nSeu nome tem \033[1;33m{}\033[0m letras\nSeu primeiro nome tem \033[1;36m{}\033[0m letras.".format(nome_completo.upper(), nome_completo.lower(), len(nome_completo.replace(" ", "")), len(nome_completo.split()[0])))
