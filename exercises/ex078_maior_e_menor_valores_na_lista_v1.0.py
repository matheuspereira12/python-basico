numeros = []

for i in range(1, 6):
    numeros.append(int(input(f"Digite o {i}º número inteiro: ")))
    
print(f"O menor número digitado foi {min(numeros)} e o maior número digitado foi {max(numeros)}.\nA posição do menor número na lista é {numeros.index(min(numeros))} e a do maior número é {numeros.index(max(numeros))}.")