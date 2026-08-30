# Verifica e exibe o menor e o maior entre os três números informados.


numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))
numero_3 = int(input("Digite o terceiro número: "))

if numero_2 < numero_1 and numero_2 < numero_3:
    print("O menor número é: \033[1;32m{}\033[0m.".format(numero_2))
elif numero_3 < numero_1 and numero_3 < numero_2:
    print("O menor número é: \033[1;32m{}\033[0m.".format(numero_3))
else:
    print("O menor número é: \033[1;32m{}\033[0m.".format(numero_1))
if numero_2 > numero_1 and numero_2 > numero_3:
    print("O maior número é: \033[1;36m{}\033[0m.".format(numero_2))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print("O maior número é: \033[1;36m{}\033[0m.".format(numero_3))
else:
    print("O maior número é: \033[1;36m{}\033[0m.".format(numero_1))