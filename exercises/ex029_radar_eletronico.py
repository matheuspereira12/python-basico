
# Verifica a velocidade do carro e calcula a multa caso ultrapasse o limite de 80 km/h.

velocidade = int(input("Digite a velocidade do carro em km/h: "))


print("Você ultrapassou o limite de 80 km/h!\nVocê foi multado!\nO valor da multa foi de R$ {}.".format((velocidade - 80) * 7) if velocidade > 80 else "Você está dentro do limite de velocidade de 80 km/h.\nVocê não foi multado!")
