# Calcula e exibe o dobro, o triplo e a raiz quadrada do valor informado pelo usuário.

num = int(input("Digite qualquer valor:\n"))
print("O dobro de \033[1;36;40m{}\033[0m é \033[33;40m{}\033[0m.\nO triplo é \033[32;40m{}\033[0m.\nA raiz quadrada é \033[35;40m{}\033[0m.".format(num, (num * 2), (num * 3), (num ** 0.5)))
