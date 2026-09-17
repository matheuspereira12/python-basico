while True:
    valor_saque = int(input("Digite o valor que você deseja sacar: "))
    qtd_cedulas_50 = valor_saque // 50
    valor_saque -= qtd_cedulas_50 * 50
    qtd_cedulas_20 = valor_saque // 20
    valor_saque -= qtd_cedulas_20 * 20
    qtd_cedulas_10 = valor_saque // 10
    valor_saque -= qtd_cedulas_10 * 10
    qtd_cedulas_1 = valor_saque // 1
    valor_saque -= qtd_cedulas_1 * 1
    print(f"Cédulas entregues: R$ 50,00: {qtd_cedulas_50} | R$ 20,00: {qtd_cedulas_20} | R$ 10,00: {qtd_cedulas_10} | R$ 1,00: {qtd_cedulas_1}")
    while True:
        continuar_saque = input("Deseja realizar outro saque? [S/N]: ").strip().upper()
        if continuar_saque == "S" or continuar_saque == "N":
            break
        print("Opção inválida! Digite apenas S ou N: ")
    if continuar_saque == "N":
        break
    
print("Obrigado por utilizar nosso caixa eletrônico. Até a próxima!")