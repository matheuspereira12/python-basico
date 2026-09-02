# Calcula o resultado de uma partida de Pedra, Papel e Tesoura.

from random import randint


jogador = int(input("[1] Pedra\n[2] Papel\n[3] Tesoura\nEscolha uma opção:"))
computador = randint(1, 3)

if jogador == 1 and computador == 1:
    print("Empate! Pedra e Pedra!")
elif jogador == 1 and computador == 2:
    print("Jogador escolheu Pedra. Computador escolheu Papel. Você perdeu!")
elif jogador == 1 and computador == 3:
    print("Jogador escolheu Pedra. Computador escolheu Tesoura. Você venceu!")
elif jogador == 2 and computador == 2:
    print("Empate! Papel e Papel!")
elif jogador == 2 and computador == 1:
    print("Jogador escolheu Papel. Computador escolheu Pedra. Você venceu!")
elif jogador == 2 and computador == 3:
    print("Jogador escolheu Papel. Computador escolheu Tesoura. Você perdeu!")
elif jogador == 3 and computador == 3:
    print("Empate! Tesoura e Tesoura!")
elif jogador == 3 and computador == 1:
    print("Jogador escolheu Tesoura. Computador escolheu Pedra. Você perdeu!")
elif jogador == 3 and computador == 2:
    print("Jogador escolheu Tesoura. Computador escolheu Papel. Você venceu!")
else:
    print("Opção inválida!")