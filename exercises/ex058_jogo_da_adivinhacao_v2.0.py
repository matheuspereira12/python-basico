# Jogo da adivinhação: o usuário tenta descobrir o número sorteado entre 0 e 10.


from random import randint

numero_sorteado = randint(0, 10)
quantidade_tentativas = 0
continuar_jogo = True

while continuar_jogo:
    numero_digitado = int(input("Digite um número entre 0 e 10: "))
    quantidade_tentativas += 1
    if numero_digitado != numero_sorteado:
        print("Você errou! Tente novamente.")
    else:
        print("Parabéns! Você acertou o número sorteado em {} tentativas. O número sorteado era {}.".format(quantidade_tentativas, numero_sorteado))
        continuar_jogo = False