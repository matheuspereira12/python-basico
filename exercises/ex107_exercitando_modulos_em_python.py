import moeda

opcao = int(input("Digite uma opção:\n\n1 - Aumentar o valor em 10%\n2 - Diminuir o valor em 10%\n3 - Dobrar o valor\n4 - Calcular a metade do valor: "))
numero = float(input("Digite um valor: "))
if opcao == 1:
    print(f"O resultado é {moeda.aumentar(numero=numero)}.")
elif opcao == 2:
    print(f"O resultado é {moeda.diminuir(numero=numero)}.")
elif opcao == 3:
    print(f"O resultado é {moeda.dobro(numero=numero)}.")
else:
    print(f"O resultado é {moeda.metade(numero=numero)}.")
    