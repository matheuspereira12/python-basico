# Soma os números pares entre os 6 números digitados pelo usuário.

soma = 0

for i in range(6):
    numero = int(input("Digite um número inteiro qualquer:"))
    if numero % 2 == 0:
        soma += numero
        
print("A soma dos números pares é {}.".format(soma))
