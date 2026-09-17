numeros_extensos = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

while True:
    numero = int(input("Digite um número entre 0 e 20:"))
    if numero >= 0 and numero <= 20:
        break
    print("\033[31mATENÇÃO!\033[0m DIGITE UM NÚMERO ENTRE 0 E 20.")
    
print(f"Você digitou o número {numeros_extensos[numero]}.")