# Converte um número inteiro para binário, octal ou hexadecimal conforme a escolha do usuário.

numero = int(input("Digite um número inteiro qualquer: "))
base = int(input("Escolha a base de conversão (1 para binário, 2 para octal e 3 para hexadecimal): "))

if base == 1:
    print("O valor em binário é: {}.".format(bin(numero)[2:]))
elif base == 2:
    print("O valor em octal é: {}.".format(oct(numero)[2:]))
elif base == 3:
    print("O valor em hexadecimal é: {}.".format(hex(numero)[2:]))
else:
    print("\033[31mOpção inválida\033[0m. Tente novamente.")