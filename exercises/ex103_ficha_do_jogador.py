def ficha_do_jogador(nome, gols=0):
    if nome == "":
        nome = "desconhecido"
    return f"O jogador {nome} fez {gols} gols."


nome_jogador = input("Digite o nome do jogador: ").strip().capitalize()
quantidade_gols = int(input("Digite a quantidade de gols:"))
print(ficha_do_jogador(nome_jogador, quantidade_gols))