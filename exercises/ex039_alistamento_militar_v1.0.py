from datetime import date

ano_nascimento = int(input("Ano de nascimento: "))
idade = date.today().year - ano_nascimento

if idade == 18:
    print("Quem nasceu em {} tem 18 anos em {}. Sendo assim, você deve se alistar imediatamente!".format(ano_nascimento, date.today().year))
elif idade < 18:
    print("Quem nasceu em {} tem {} anos em {}. Ainda faltam {} anos para o alistamento.".format(ano_nascimento, idade, date.today().year, 18 - idade))
else:
    print("Quem tem {} anos já deveria ter se alistado há {} anos.".format(idade, idade - 18))
    