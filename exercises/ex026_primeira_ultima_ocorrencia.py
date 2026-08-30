
# Analisa a quantidade e a primeira e última ocorrência da letra A na frase.

frase = input("Digite uma frase: ").strip().upper()
frase = frase.replace("Á", "A").replace("À", "A").replace("Ã", "A").replace("Â", "A")

print("A letra A aparece \033[1;32m{}\033[0m vezes.\nA letra A aparece pela primeira vez na \033[1;33m{}\033[0mª posição.\nA letra A aparece pela última vez na \033[1;36m{}\033[0mª posição.".format(frase.count("A"), frase.find("A") + 1, frase.rfind("A") + 1))
