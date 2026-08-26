# Calcula a hipotenusa a partir dos valores dos catetos.

from math import hypot

cateto_oposto = float(input("Digite o valor do cateto oposto: "))
cateto_adjacente = float(input("Digite o valor do cateto adjacente: "))


hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print("O valor da hipotenusa é: {:.2f}.".format(hipotenusa))
