def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f"A área do terreno é de {area_terreno:.2f} metros quadrados.")


largura = float(input("Digite a largura do terreno em metros: ").replace(",", "."))
comprimento = float(input("Digite o comprimento do terreno em metros: ").replace(",", "."))

area(largura, comprimento)