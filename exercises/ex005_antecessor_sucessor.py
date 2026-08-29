# Calcula e exibe o antecessor e o sucessor do número informado pelo usuário.

num = int(input("Digite um número:\n"))
print("O antecessor de \033[1;36;40m{}\033[0m é \033[33;40m{}\033[0m e o sucessor é \033[32;40m{}\033[0m.".format(num, num - 1, num + 1))
