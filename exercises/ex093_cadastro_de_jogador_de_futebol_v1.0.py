jogador = dict()

jogador["nome"] = input("Digite o nome do jogador: ").strip().capitalize()

quantidade_partidas = int(input("Digite a quantidade de partidas que o jogador disputou: "))
jogador["partidas"] = quantidade_partidas
jogador["gols"] = list()

for i in range(1, quantidade_partidas + 1):
    jogador["gols"].append(int(input(f"Digite a quantidade de gols marcados na {i}ª partida: ")))
    
jogador["total_gols"] = sum(jogador["gols"])

print(f'O jogador {jogador["nome"]} disputou {jogador["partidas"]} partidas e marcou um total de {jogador["total_gols"]} gols.')
