# Solicita a cidade de nascimento, pega os 5 primeiros caracteres e verifica se eles formam "SANTO".

cidade_nascimento = str(input("Digite a cidade onde você nasceu: ").strip().upper()[:5])

print("A cidade de nascimento contém a palavra 'Santo': {}".format("SANTO" in cidade_nascimento))
