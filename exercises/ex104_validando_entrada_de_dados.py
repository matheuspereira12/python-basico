def leia_int():
    while True:
        numero = input("Digite um número inteiro: ").strip()
        if numero.removeprefix("-").isnumeric():
            return int(numero)
        print("Digite um número inteiro válido:\n")
        
        
leia_int()