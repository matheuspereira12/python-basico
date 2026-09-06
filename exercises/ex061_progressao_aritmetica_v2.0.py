# Exibe os 10 primeiros termos de uma Progressão Aritmética (PA)

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
contador = 0


while contador < 10:
    print(primeiro_termo)
    primeiro_termo += razao
    contador += 1