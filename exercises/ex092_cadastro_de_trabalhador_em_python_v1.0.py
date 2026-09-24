from datetime import date
trabalhador = dict()

trabalhador["Nome"] = input("Digite o nome do trabalhador: ").strip().capitalize()
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = date.today().year - ano_nascimento
trabalhador["Idade"] = idade
numero_carteira_trabalho = int(input("Digite o número da carteira de trabalho (0 caso não possua): "))
if numero_carteira_trabalho != 0:
    trabalhador["Carteira"] = numero_carteira_trabalho
    ano_contratacao = int(input("Digite o ano de contratação: "))
    trabalhador["Ano"] = ano_contratacao
    salario = float(input("Digite o salário: R$ "))
    trabalhador["Salario"] = salario
    trabalhador["Aposentadoria"] = ((ano_contratacao + 35) - date.today().year) + idade
    print(
    f'Nome do trabalhador: {trabalhador["Nome"]}.\n'
    f'Idade: {trabalhador["Idade"]} anos.\n'
    f'Número da carteira de trabalho: {trabalhador["Carteira"]}.\n'
    f'Salário: R$ {trabalhador["Salario"]:.2f}.\n'
    f'Ano previsto para aposentadoria: {trabalhador["Aposentadoria"]}.'
)
else:
    print(
    f'Nome do trabalhador: {trabalhador["Nome"]}.\n'
    f'Idade: {trabalhador["Idade"]} anos.'
)