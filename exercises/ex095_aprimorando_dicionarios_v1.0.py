jogador = list()
contador = 0

while True:
    jogador.append(dict())
    jogador[contador]["nome"] = input("Digite o nome do jogador: ").strip().capitalize()
    quantidade_partidas = int(input("Digite a quantidade de partidas que o jogador disputou: "))
    jogador[contador]["partidas"] = quantidade_partidas
    jogador[contador]["gols"] = list()
    for i in range(1, quantidade_partidas + 1):
        jogador[contador]["gols"].append(int(input(f"Digite a quantidade de gols marcados na {i}ª partida: ")))
    jogador[contador]["total_gols"] = sum(jogador[contador]["gols"])
    contador += 1
    while True:
        continuar = input("Deseja cadastrar outro jogador? (S/N): ").strip().upper()
        if continuar == "S" or continuar == "N":
            break
    if continuar == "N":
        break

while True:
    nome_busca = input("Digite o nome do jogador que deseja consultar (999 para encerrar): ").strip().capitalize()
    if nome_busca == "999":
        break
    else:
        for p in jogador:
            if p["nome"] == nome_busca:
                print(f'O jogador {p["nome"]} disputou {p["partidas"]} partidas e marcou um total de {p["total_gols"]} gols.')
                