# Calcula o salário com reajuste de 15%

salario = float(input("Digite o salário do funcionário: R$ "))
salario_reajustado = salario * 1.15
print("O salário com reajuste de 15% será R$ \033[1;32m{:.2f}\033[0m.".format(salario_reajustado))
