# Embaralha aleatoriamente a lista de alunos e exibe a ordem sorteada.

from random import shuffle

aluno_1 = input("Digite o nome do primeiro aluno: ")
aluno_2 = input("Digite o nome do segundo aluno: ")
aluno_3 = input("Digite o nome do terceiro aluno: ")
aluno_4 = input("Digite o nome do quarto aluno: ")

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista_alunos)

print("A ordem sorteada foi:\n{:<20} \n{:<20} \n{:<20} \n{:<20}".format(lista_alunos[0], lista_alunos[1], lista_alunos[2], lista_alunos[3]))

