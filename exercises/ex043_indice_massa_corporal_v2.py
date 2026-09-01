# Calcula o IMC e classifica o resultado de acordo com a faixa correspondente.

peso = float(input("Digite seu peso em kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

imc = peso / pow(altura, 2)

if imc < 18.5:
    print("Seu IMC é {:.1f}.\nClassificação: Abaixo do peso.".format(imc))
elif imc < 25:
    print("Seu IMC é {:.1f}.\nClassificação: Peso normal.".format(imc))
elif imc < 30:
    print("Seu IMC é {:.1f}.\nClassificação: Sobrepeso.".format(imc))
else:
    print("Seu IMC é \033[1;31m{:.1f}\033[0m.\nClassificação: Obesidade.".format(imc))