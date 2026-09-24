from random import randint
from time import sleep
from operator import itemgetter

jogador = dict()

for i in range(1, 5):
    jogador[input(f"Digite o nome do jogador {i}: ").strip().capitalize()] = randint(1, 6)
    
    
    
    
resultados_ordenados = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for nome, numero in resultados_ordenados:
    print(f"{nome} sorteou o número {numero} no dado.")
    sleep(1)
    