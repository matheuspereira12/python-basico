# Soma e conta os números digitados, encerrando quando o usuário digitar 999.

soma_total= 0
contador = 0
continuar = True

while continuar:
    numero = int(input("Digite um número inteiro qualquer para ser somado: "))
    if numero == 999:
        continuar = False
    else:
        soma_total += numero
        contador += 1
        
print("Total de números digitados: {} | Total somado: {}".format(contador, soma_total))
