def contador(inicio, fim, passo):
    print(f"Contagem de {inicio} até {fim}.\n")
    contagem = list()
    for i in range(inicio, fim + 1, passo):
        contagem.append(i)
    contagem = ", ".join(map(str, contagem))
    print(f"Os números escolhidos foram {contagem}.")
    
    
inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))
passo = int(input("Digite o passo da contagem: "))

contador(inicio, fim, passo)
