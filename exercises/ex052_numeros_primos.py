# Verifica se o número é primo ou não.

numero = int(input("Digite um número: "))
divisores = 0

for i in range(2, numero):
    if numero % i == 0:
        divisores += 1

if numero == 1 or numero == 0:
    print("Não é primo.")
elif divisores == 0:
    print("É primo.")
else:
    print("Não é primo.")
    