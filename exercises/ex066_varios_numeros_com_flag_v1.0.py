quantidade_numeros = 0
total = 0

while True:
    numero = int(input("Digite um número inteiro (999 para encerrar): "))
    if numero == 999:
        print(f"Você digitou {quantidade_numeros} números ao todo, e a soma dos valores digitados foi {total}.")
        break
    else:
        quantidade_numeros += 1
        total += numero
        