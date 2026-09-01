# Compara dois valores e informa qual é maior ou se são iguais.

primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))

if primeiro_valor > segundo_valor:
    print("\033[1;33m{}\033[0m é maior que \033[1;33m{}\033[0m.".format(primeiro_valor, segundo_valor))
elif segundo_valor > primeiro_valor:
    print("\033[1;33m{}\033[0m é maior que \033[1;33m{}\033[0m.".format(segundo_valor, primeiro_valor))
else:
    print("\033[1;33m{}\033[0m é igual a \033[1;33m{}\033[0m.".format(primeiro_valor, segundo_valor))
    