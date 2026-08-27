
# Analisa a quantidade e a primeira e última ocorrência da letra A na frase.

frase = str(input("Digite uma frase: ")).strip().upper()

print("A letra A aparece {} vezes.\nA letra A aparece pela primeira vez na {}ª posição.\nA letra A aparece pela última vez na {}ª posição.".format(frase.count("A"), frase.find("A") + 1, frase.rfind("A") + 1))
