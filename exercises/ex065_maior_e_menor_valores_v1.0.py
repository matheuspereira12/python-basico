# Calcula a média, o menor e o maior valor digitado

continuar = True
soma_total, contador, menor_valor, maior_valor = 0, 0, 0, 0

while continuar:
    numero = int(input("Digite um número inteiro qualquer: "))
    soma_total += numero
    contador += 1
    if contador == 1:
        menor_valor = numero
        maior_valor = numero
    else:
        if numero < menor_valor:
            menor_valor = numero
        if numero > maior_valor:
            maior_valor = numero
    continuar_somando = input("Quer continuar somando? (S/N):").strip().upper()
    if continuar_somando == "N":
        continuar = False
            
print("A média dos valores é {:.2f}, o menor valor é {} e o maior valor é {}.".format(soma_total / contador, menor_valor, maior_valor))