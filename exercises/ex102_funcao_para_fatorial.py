def fatorial(n=0, show=False):
    if n == 0 or n == 1:
        return 1
    elif show == False:
        resultado = 0
        for x, y in enumerate(range(n, 2, -1)):
            if x == 0:
                resultado = y * (y - 1)
            else:
                resultado = resultado * (y - 1)
        return resultado
    else:
        resultado = 0
        etapas = list()
        for x, y in enumerate(range(n, 2, -1)):
            if x == 0:
                resultado = y * (y - 1)
                etapas.append(resultado)
            else:
                resultado = resultado * (y - 1)
                etapas.append(resultado)
        return etapas


numero = int(input("Digite um número para calcular o fatorial: "))
while True:
    mostrar_calculo = input("Deseja ver o cálculo? (S/N): ").strip().upper()
    if mostrar_calculo == "S" or mostrar_calculo == "N":
        break
if mostrar_calculo== "S":
    calculo_formatado = ", ".join(map(str, fatorial(numero, True)))
    print(f"O cálculo do fatorial de {numero} foi: {calculo_formatado}.")
else:
    print(f"O cálculo do fatorial de {numero} foi: {fatorial(numero)}.")