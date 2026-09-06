# Melhorando o exercício anterior

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
contador = 0
continuar = True
quantidade_termos = 10

while continuar:
    print(primeiro_termo)
    primeiro_termo += razao
    contador += 1
    if contador == quantidade_termos:
        quantidade_termos = int(input("Quer continuar mostrando mais termos da PA? Digite 0 para encerrar ou a quantidade de termos que deseja ver: "))
        if quantidade_termos == 0:
            continuar = False
        else:
            quantidade_termos += contador