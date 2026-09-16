from random import randint


while True:
    escolha_computador = randint(1, 2)
    numero_computador = randint(1, 10)
    escolha_jogador = int(input("Escolha sua opção: 1 para Par ou 2 para Ímpar: "))
    numero_jogador = int(input("Digite o número que você deseja jogar (1 a 10): "))
    soma = numero_jogador + numero_computador
    if escolha_jogador == 1 and soma % 2 == 0:
        print("Você escolheu Par e a soma também é Par. Você ganhou!")
    elif escolha_jogador == 2 and soma % 2 == 1:
        print("Você escolheu Ímpar e a soma também é Ímpar. Você ganhou!")
    else:
        print("Você perdeu! A soma não corresponde à sua escolha.")
        break