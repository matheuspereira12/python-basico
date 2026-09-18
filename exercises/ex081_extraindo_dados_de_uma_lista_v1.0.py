numeros = []

while True:
    valor = input("Digite um valor inteiro ou pressione Enter para encerrar: ")
    if valor == "":
        break
    numeros.append(int(valor))
    
numeros.sort(reverse=True)
print(f"A quantidade de valores digitados foi {len(numeros)}.")
print("Os valores digitados foram:")
for i in numeros:
    print(i)
    
if 5 in numeros:
    print("O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")