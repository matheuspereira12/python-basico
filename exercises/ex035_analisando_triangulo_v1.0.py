# Verifica se os três segmentos de reta podem formar um triângulo.

segmento1 = float(input("Digite o comprimento do primeiro segmento de reta: ").replace(",", "."))
segmento2 = float(input("Digite o comprimento do segundo segmento de reta: ").replace(",", "."))
segmento3 = float(input("Digite o comprimento do terceiro segmento de reta: ").replace(",", "."))

print("É possível formar um triângulo com esses três segmentos de reta." if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2 else "Não é possível formar um triângulo com esses três segmentos de reta.")
