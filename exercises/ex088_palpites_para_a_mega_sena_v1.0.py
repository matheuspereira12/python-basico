from random import randint

jogos = []

quantidade_jogos = int(input("Digite a quantidade de jogos a serem gerados: "))

for i in range(quantidade_jogos):
    jogos.append([])
    while len(jogos[i]) < 6:
        palpite = randint(1, 60)
        if palpite not in jogos[i]:
            jogos[i].append(palpite)
            
            
for i in jogos:
    resultado_jogo = ", ".join(map(str, i))
    print(resultado_jogo)
    