# Calcula o valor da passagem de acordo com a distância da viagem.

print("Olá! Seja bem-vindo à nossa empresa de ônibus!\n\nPara calcular o valor da sua viagem, consideramos a distância percorrida. Em viagens de até 200 km, o valor é de R$ 0,50 por quilômetro. Para viagens com mais de 200 km, o valor é de R$ 0,45 por quilômetro.\n\nInforme a distância da sua viagem e descubra o valor da passagem!\n")

distancia_viagem = float(input("Digite a distância da sua viagem em km: "))
print("\033[1;32mSua viagem tem até 200 km.\nO valor total da passagem é de R$ {:.2f}.\033[0m".format(distancia_viagem * 0.5) if distancia_viagem <= 200 else "\033[1;33mSua viagem tem mais de 200 km.\nO valor total da passagem é de R$ {:.2f}.\033[0m".format(distancia_viagem * 0.45))
