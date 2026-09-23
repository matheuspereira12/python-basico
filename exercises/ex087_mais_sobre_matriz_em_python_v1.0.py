matriz = [[], [], []]
pares = 0
soma_terceira_coluna = 0

for i in range(1, 10):
    valor = int(input(f"Digite o valor do elemento {i}: "))
    if i <= 3:
        matriz[0].append(valor)
    elif i <= 6:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
        
        
for linha in matriz:
    soma_terceira_coluna += linha[2]
    for item in linha:
        if item % 2 == 0:
            pares += item
            
maior_segunda_linha = max(matriz[1])

print(f"A soma dos números pares da matriz é {pares}.\nA soma dos valores da terceira coluna é {soma_terceira_coluna}.\nO maior valor da segunda linha é {maior_segunda_linha}.\n")

print(f"{matriz[0][0]:^5}{matriz[0][1]:^5}{matriz[0][2]:^5}\n{matriz[1][0]:^5}{matriz[1][1]:^5}{matriz[1][2]:^5}\n{matriz[2][0]:^5}{matriz[2][1]:^5}{matriz[2][2]:^5}")