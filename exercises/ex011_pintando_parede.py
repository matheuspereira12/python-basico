

altura_parede = float(input("Digite a altura da parede:\n"))
largura_parede = float(input("Digite a largura da parede:\n"))
area_parede = altura_parede * largura_parede

print("A área da sua parede é \033[1;34m{:.1f}\033[0m m².\nVocê vai precisar de \033[1;33m{:.1f}\033[0m litros de tinta para pintar.".format(area_parede, area_parede / 2))
# Dependendo da qualidade da tinta, talvez precise de mais kkk
