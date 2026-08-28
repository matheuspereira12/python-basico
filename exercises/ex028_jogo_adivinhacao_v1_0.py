# Jogo de adivinhação: o usuário tenta acertar o número sorteado entre 0 e 5.

from random import randint
print("Seja bem-vindo ao Jogo da Adivinhação!\nEscolha um número de 0 a 5 e tente adivinhar o número que será sorteado.\n")

numero_digitado = int(input("Digite um número de 0 a 5: ").strip())

numero_sorteado = randint(0, 5)

print("Parabéns! Você acertou!\nO número sorteado foi {}.".format(numero_sorteado) if numero_digitado == numero_sorteado else "Que pena! Você errou!\nO número sorteado foi {}.".format(numero_sorteado))
