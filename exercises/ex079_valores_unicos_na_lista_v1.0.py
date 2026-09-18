numeros = []

while True:
    valor = input("Digite um valor inteiro ou pressione Enter para encerrar: ")
    if valor == "":
        break
    if valor in numeros:
        print("Esse número já foi digitado.")
    else:
        numeros.append(int(valor))
            
numeros.sort()
print("Os números em ordem crescente são:")
for i in numeros:
    print(i)