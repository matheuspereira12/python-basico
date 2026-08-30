from random import choice

aluno_1 = input("Digite o nome do primeiro aluno: ")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceiro aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")

aluno_sorteado = choice([aluno_1, aluno_2, aluno_3, aluno_4])

print("O aluno sorteado foi: \033[1;33m{}\033[0m!".format(aluno_sorteado))
