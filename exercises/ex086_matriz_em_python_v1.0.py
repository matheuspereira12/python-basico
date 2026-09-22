matriz = [[], [], []]

for i in range(1, 10):
    valor = int(input(f"Digite o valor do elemento {i}: "))
    if i <= 3:
        matriz[0].append(valor)
    elif i <= 6:
        matriz[1].append(valor)
    else:
        matriz[2].append(valor)
        
print(f"{matriz[0][0]:^5}{matriz[0][1]:^5}{matriz[0][2]:^5}\n{matriz[1][0]:^5}{matriz[1][1]:^5}{matriz[1][2]:^5}\n{matriz[2][0]:^5}{matriz[2][1]:^5}{matriz[2][2]:^5}")