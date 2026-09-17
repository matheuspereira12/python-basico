numeros = (int(input("Digite um valor inteiro: ")), int(input("Digite um valor inteiro: ")), int(input("Digite um valor inteiro: ")), int(input("Digite um valor inteiro: ")))

print(f"O número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O número 3 foi digitado pela primeira vez na {numeros.index(3) + 1}ª posição.")
else:
    print("O número 3 não foi digitado.")
    
print("Os números pares são:")
for i in numeros:
    if i % 2 == 0:
        print(i)