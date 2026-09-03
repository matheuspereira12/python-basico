# Percorre a frase de trás para frente e monta a string invertida

frase = input("Digite uma frase para verificar se ela é um palíndromo: ").lower().replace(" ", "").replace(",", "").replace(".", "").replace("!", "")
inverso = ""

for letra in range(len(frase) - 1, -1, -1):
    inverso += frase[letra]
    

if inverso == frase:
    print("A frase é um palíndromo!")
else:
    print("A frase não é um palíndromo!")
    