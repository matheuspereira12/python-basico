# Calcula o novo salário aplicando 15% de aumento para salários de até R$ 1.250,00 e 10% para salários acima desse valor.


salario = float(input("Digite o seu salário: "))
print("O salário do funcionário era R$ {:.2f}.\nCom o aumento, o novo salário será R$ {:.2f}.".format(salario, salario * 1.15) if salario <= 1250.0 else "O salário do funcionário era R$ {:.2f}.\nCom o aumento, o novo salário será R$ {:.2f}.".format(salario, salario * 1.1))
