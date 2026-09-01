
# Verifica se três segmentos podem formar um triângulo e classifica-o como equilátero, isósceles ou escaleno.


segmento1 = float(input("Digite o comprimento do primeiro segmento de reta: ").replace(",", "."))
segmento2 = float(input("Digite o comprimento do segundo segmento de reta: ").replace(",", "."))
segmento3 = float(input("Digite o comprimento do terceiro segmento de reta: ").replace(",", "."))


if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    if segmento1 == segmento2 and segmento1 == segmento3:
        print("É possível formar um triângulo equilátero com esses três segmentos de reta.")
    elif segmento1 != segmento2 and segmento1  != segmento3 and segmento2 != segmento3:
        print("É possível formar um triângulo escaleno com esses três segmentos de reta.")
    else:
        print("É possível formar um triângulo isósceles com esses três segmentos de reta.")
else:
    print("Não é possível formar um triângulo com esses três segmentos de reta.")