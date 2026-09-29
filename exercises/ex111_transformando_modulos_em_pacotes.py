from utilidadesmoeda import moeda, resumo

opcao = int(input("Digite uma opção:\n\n1 - Aumentar o valor em 10%\n2 - Diminuir o valor em 10%\n3 - Dobrar o valor\n4 - Calcular a metade do valor: "))
numero = float(input("Digite um valor: "))
formatar = input("Deseja visualizar o texto formatado? (S/N): ").strip().upper()

exibir_formatado = formatar == "S"

if opcao == 1:
    resultado = moeda.aumentar(numero=numero, exibir_formatado=exibir_formatado)
elif opcao == 2:
    resultado = moeda.diminuir(numero=numero, exibir_formatado=exibir_formatado)
elif opcao == 3:
    resultado = moeda.dobro(numero=numero, exibir_formatado=exibir_formatado)
else:
    resultado = moeda.metade(numero=numero, exibir_formatado=exibir_formatado)

print(resultado)

print(resumo.resumo(numero))