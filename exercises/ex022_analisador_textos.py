# Solicita o nome completo e exibe informações sobre ele, como maiúsculas, minúsculas e quantidade de letras.

nome_completo = input("Digite seu nome completo:\n").strip()

print("Seu nome com letras maiúsculas é {}\nSeu nome com letras minúsculas é {}\nSeu nome tem {} letras\nSeu primeiro nome tem {} letras".format(nome_completo.upper(), nome_completo.lower(), len(nome_completo.replace(" ", "")), len(nome_completo.split()[0])))
