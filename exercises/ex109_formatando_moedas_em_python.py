import moeda

opcao = int(input("Digite uma opção:\n\n1 - Aumentar o valor em 10%\n2 - Diminuir o valor em 10%\n3 - Dobrar o valor\n4 - Calcular a metade do valor: "))
numero = float(input("Digite um valor: "))
formatar = input("Deseja visualizar o texto formatado? (S/N): ").strip().upper()
if formatar == "S":
    if opcao == 1:
        print(moeda.aumentar(numero=numero, exibir_formatado=True))
    elif opcao == 2:
        print(moeda.diminuir(numero=numero, exibir_formatado=True))
    elif opcao == 3:
        print(moeda.dobro(numero=numero, exibir_formatado=True))
    else:
        print(moeda.metade(numero=numero, exibir_formatado=True))
else:
    if opcao == 1:
        print(moeda.aumentar(numero=numero))
    elif opcao == 2:
        print(moeda.diminuir(numero=numero))
    elif opcao == 3:
        print(moeda.dobro(numero=numero))
    else:
        print(moeda.metade(numero=numero))
