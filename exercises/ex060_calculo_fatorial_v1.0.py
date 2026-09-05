# Calcula o fatorial do número informado pelo usuário.

numero = int(input("Digite um número inteiro para calcular o seu fatorial: "))
produto = numero
multiplicador = numero - 1

while multiplicador != 0:
    produto_parcial = produto * multiplicador
    multiplicador -= 1
    produto = produto_parcial
    
    
print("O fatorial de {} é {}.".format(numero, produto))