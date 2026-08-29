# Soma dois números e exibe o resultado.

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))
soma = num1 + num2
print("A soma entre {} e {} é \033[32;44m{}.\033[0m".format(num1, num2, soma))
