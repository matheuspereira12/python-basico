

altura_parede = float(input("Digite a altura da parede:\n"))
largura_parede = float(input("Digite a largura da parede:\n"))
area_parede = altura_parede * largura_parede

print("A área da sua parede é {:.1f} m².\nVocê vai precisar de {:.1f} litros de tinta para pintar.\n".format(area_parede, area_parede / 2))
# Dependendo da qualidade da tinta, talvez precise de mais kkk
