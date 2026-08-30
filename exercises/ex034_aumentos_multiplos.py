# Calcula o novo salário aplicando 15% de aumento para salários de até R$ 1.250,00 e 10% para salários acima desse valor.


salario = float(input("Digite o seu salário: "))
print("\033[1;32mO salário do funcionário era R$ {:.2f}.\nCom o aumento, o novo salário será R$ {:.2f}.\033[0m".format(salario, salario * 1.15) if salario <= 1250.0 else "\033[1;33mO salário do funcionário era R$ {:.2f}.\nCom o aumento, o novo salário será R$ {:.2f}.\033[0m".format(salario, salario * 1.1))
