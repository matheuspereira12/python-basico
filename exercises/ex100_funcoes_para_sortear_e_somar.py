from random import randint

numeros_sorteados = list()


def sorteador(lista):
    for i in range(0, 5):
        lista.append(randint(1, 5))


def soma_par(lista):
    total_pares = 0
    for i in lista:
        if i % 2 == 0:
            total_pares += i
    return total_pares
            
            
sorteador(numeros_sorteados)
numeros_formatados = ", ".join(map(str, numeros_sorteados))


print(f"Os números sorteados foram: {numeros_formatados}.")
print(f"A soma dos números pares sorteados é: {soma_par(numeros_sorteados)}.")

