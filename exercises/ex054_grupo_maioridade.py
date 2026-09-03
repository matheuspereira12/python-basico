# Conta a quantidade de pessoas maiores e menores de idade.

from datetime import date

maiores_idade = 0
menores_idade = 0

for i in range(7):
    ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
    if (date.today().year - ano_nascimento) >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1
        
print("A quantidade de pessoas maiores de idade é {} e a de menores de idade é {}.".format(maiores_idade, menores_idade))
