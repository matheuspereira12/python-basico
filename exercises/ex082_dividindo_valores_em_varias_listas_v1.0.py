numeros = []
numeros_pares = []
numeros_impares = []

while True:
    valor = input("Digite um valor ou pressione Enter para encerrar: ")
    if valor == "":
        break
    numeros.append(int(valor))
    
for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)
        
print("Os números pares são:")
for n in numeros_pares:
    print(n)
print("Os números ímpares são:")
for n in numeros_impares:
    print(n)