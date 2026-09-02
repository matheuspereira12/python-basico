# Exibe os 10 primeiros termos da PA

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))

for i in range(10):
    print(primeiro_termo)
    primeiro_termo += razao