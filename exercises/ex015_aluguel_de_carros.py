# O aluguel custa R$ 60 por dia e R$ 0,15 por quilômetro rodado.    

dias_aluguel = int(input("Digite a quantidade de dias que o carro foi alugado:\n"))
km_rodados = int(input("Digite a quantidade de quilômetros rodados:"))
valor_total = (dias_aluguel * 60) + (km_rodados * 0.15)

print("O valor total a pagar pelo aluguel é: R$ {:.2f}".format(valor_total))
