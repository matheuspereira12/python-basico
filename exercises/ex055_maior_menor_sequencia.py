# Analisa os pesos informados e identifica o menor e o maior peso.

menor_peso = 0
maior_peso = 0

for i in range(1, 6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(i)))
    if i == 1:
        menor_peso = peso
        maior_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:                
            menor_peso = peso
            
print("O menor peso foi de {} kg, e o maior peso foi de {} kg.".format(menor_peso, maior_peso))