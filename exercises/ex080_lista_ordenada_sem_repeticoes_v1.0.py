numeros = []

for i in range(1, 6):
    while True:
        valor = int(input(f"Digite o {i}º valor:"))
        if valor not in numeros:
            break
        print("Esse valor já foi digitado. Digite outro valor:")
    if i == 1:
        numeros.append(valor)
    else:
        if valor < min(numeros):
            numeros.insert(0, valor)
        if valor > min(numeros) and valor < max(numeros):
            for p in range(len(numeros)):
                if valor < numeros[p]:
                    numeros.insert(p, valor)
                    break
        if valor > max(numeros):
            numeros.insert(numeros.index(max(numeros)) + 1, valor)
            
print(numeros)