# Realiza uma contagem regressiva de 10 até 1 e exibe uma mensagem de Ano Novo.

from time import sleep


for i in range(10, 0, -1):
    print(i)
    sleep(1)
    
print("Feliz Ano Novo!")