def maior(*numero):
    maior_numero = 0
    for a, b in enumerate(numero):
        if a == 0:
            maior_numero = b
        else:
            if b > maior_numero:
                maior_numero = b
    print(f"O maior número digitado é {maior_numero}.")
    
    
valores = map(int, input("Digite uma sequência de números separados por espaços: ").strip().split())
maior(*valores)

