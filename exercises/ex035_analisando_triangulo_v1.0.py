# Verifica se os três segmentos de reta podem formar um triângulo.

segmento1 = float(input("Digite o comprimento do primeiro segmento de reta: ").replace(",", "."))
segmento2 = float(input("Digite o comprimento do segundo segmento de reta: ").replace(",", "."))
segmento3 = float(input("Digite o comprimento do terceiro segmento de reta: ").replace(",", "."))

print("\033[1;32mÉ possível formar um triângulo com esses três segmentos de reta.\033[0m" if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2 else "\033[1;31mNão é possível formar um triângulo com esses três segmentos de reta.\033[0m")
