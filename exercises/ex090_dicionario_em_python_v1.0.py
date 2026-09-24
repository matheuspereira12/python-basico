alunos = {}

while True:
    nome = input("Digite o nome: ").strip().capitalize()
    media_notas = float(input("Digite a média das notas do aluno: ").replace(",", "."))
    if media_notas < 5:
        alunos[nome] = "Reprovado(a)"
    elif media_notas < 7:
        alunos[nome] = "Recuperação"
    else:
        alunos[nome] = "Aprovado(a)"
        
    while True:
        continuar = input("Deseja continuar inserindo alunos? [S/N]: ").strip().upper()
        if continuar == "S" or continuar == "N":
            break
        print("Opção inválida. Digite apenas S para sim ou N para não.\n")
    if continuar == "N":
        break
    
for n, s in alunos.items():
    print(f"{n} ficou com o resultado: {s}.")