# Programa que permite realizar operações matemáticas entre dois valores

encerrar = False

while not encerrar:
    primeiro_valor = float(input("Digite o primeiro valor: "))
    segundo_valor = float(input("Digite o segundo valor: "))
    opcao = int(input("\n[1] Somar\n[2] Multiplicar\n[3] Maior valor\n[4] Novos números\n[5] Sair\nDigite a opção desejada: "))
    if opcao == 1:
        print("Soma de {} + {} = {}.".format(primeiro_valor, segundo_valor, primeiro_valor + segundo_valor))
    elif opcao == 2:
        print("Multiplicação de {} × {} = {}.".format(primeiro_valor, segundo_valor, primeiro_valor * segundo_valor))
    elif opcao == 3:
        if primeiro_valor > segundo_valor:
            print("Maior valor: {} | Menor valor: {}.".format(primeiro_valor, segundo_valor))
        elif primeiro_valor == segundo_valor:
            print("Os valores são iguais.")
        else:
            print("Maior valor: {} | Menor valor: {}.".format(segundo_valor, primeiro_valor))
    elif opcao == 4:
        print("Novos números serão solicitados.")
    elif opcao == 5:
        print("Programa encerrado. Até a próxima!")
        encerrar = True
    else:
        print("Opção inválida! Tente novamente.")
        