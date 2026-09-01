# Calcula a idade do atleta e classifica sua categoria de acordo com a faixa etária.

from datetime import date


ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = date.today().year - ano_nascimento


if idade <= 9:
    print("O atleta é da categoria Mirim.")
elif idade <= 14:
    print("O atleta é da categoria Infantil.")
elif idade <= 19:
    print("O atleta é da categoria Júnior.")
elif idade <= 25:
    print("O atleta é da categoria Sênior.")
else:
    print("O atleta é da categoria Master.")
    