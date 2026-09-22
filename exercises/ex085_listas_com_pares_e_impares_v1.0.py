numeros = [[], []]

for i in range(7):
    valor = int(input("Digite um número inteiro: "))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
        
pares = " ".join(map(str, numeros[0]))
impares = " ".join(map(str, numeros[1]))
print(f"Os números pares são {pares}.\nOs números ímpares são {impares}.")