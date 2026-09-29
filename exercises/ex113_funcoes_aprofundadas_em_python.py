def leia_int():        
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
        except Exception:
            print("Erro! Digite um número inteiro válido.")
        else:
            return numero
        
        
def leia_float():
    while True:
        try:
            numero = float(input("Digite um número real: "))
        except Exception:
            print("Erro! Digite um número real válido.")
        else:
            return numero
        
        
leia_int()
leia_float()