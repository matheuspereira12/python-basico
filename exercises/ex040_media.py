

# Calcula a média das duas notas e informa a situação do aluno.


nota_1 = float(input("Digite a primeira nota do aluno: "))

nota_2 = float(input("Digite a segunda nota do aluno: "))

media = (nota_1 + nota_2) / 2

if media < 5:
    print("A média do aluno foi {}.\nSituação: reprovado.".format(media))
elif media < 7:
    print("A média do aluno foi {}.\nSituação: recuperação.".format(media))
else:
    print("A média do aluno foi {}.\nSituação: aprovado!".format(media))
    