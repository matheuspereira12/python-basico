
# Verifica a velocidade do carro e calcula a multa caso ultrapasse o limite de 80 km/h.

velocidade = int(input("Digite a velocidade do carro em km/h: "))


print("\033[1;31mVocê ultrapassou o limite de 80 km/h\nVocê foi multado!\033[0m\nO valor da multa foi de R$ {}.".format((velocidade - 80) * 7) if velocidade > 80 else "\033[1;32mVocê está dentro do limite de velocidade de 80 km/h.\nVocê não foi multado!\033[0m")
